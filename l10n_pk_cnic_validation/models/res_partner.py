import re

from psycopg2 import IntegrityError

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

CNIC_REGEX = re.compile(r"^\d{5}-\d{7}-\d$")
CNIC_DIGITS_REGEX = re.compile(r"^\d{13}$")
CNIC_STRIP_REGEX = re.compile(r"[\s-]+")


class ResPartner(models.Model):
    _inherit = "res.partner"

    _CNIC_DUPLICATE_ERROR_MESSAGE = "CNIC must be unique across all contacts."
    _CNIC_INVALID_FORMAT_MESSAGE = (
        "Invalid CNIC format. Enter valid Pakistani CNIC (Format: 12345-1234567-1)."
    )

    cnic = fields.Char(
        string="CNIC",
        copy=False,
        index=True,
        help="Enter valid Pakistani CNIC (Format: 12345-1234567-1)",
    )
    cnic_field_enabled = fields.Boolean(
        compute="_compute_cnic_settings",
        string="CNIC Field Enabled",
    )
    cnic_validation_enabled = fields.Boolean(
        compute="_compute_cnic_settings",
        string="CNIC Validation Enabled",
    )

    _sql_constraints = [
        (
            "res_partner_cnic_unique",
            "unique(cnic)",
            "CNIC must be unique across all contacts.",
        )
    ]

    def _auto_init(self):
        result = super()._auto_init()
        self.env.cr.execute(
            """
            CREATE INDEX IF NOT EXISTS res_partner_cnic_idx
            ON res_partner (cnic)
            WHERE cnic IS NOT NULL
            """
        )
        return result

    @api.depends("company_id", "company_id.cnic_field_enabled", "company_id.cnic_validation_enabled")
    def _compute_cnic_settings(self):
        default_company = self.env.company.sudo()
        default_flags = {
            "field": bool(default_company.cnic_field_enabled),
            "validation": bool(default_company.cnic_validation_enabled),
        }

        company_flags = {
            company.id: {
                "field": bool(company.sudo().cnic_field_enabled),
                "validation": bool(company.sudo().cnic_validation_enabled),
            }
            for company in self.mapped("company_id")
            if company
        }

        for partner in self:
            flags = company_flags.get(partner.company_id.id, default_flags)
            partner.cnic_field_enabled = flags["field"]
            partner.cnic_validation_enabled = flags["validation"]

    def _is_cnic_validation_enabled(self):
        self.ensure_one()
        company = (self.company_id or self.env.company).sudo()
        return bool(company.cnic_validation_enabled)

    @api.model
    def _normalize_cnic(self, cnic):
        if isinstance(cnic, str):
            normalized = cnic.strip()
            if not normalized:
                return False
            stripped = CNIC_STRIP_REGEX.sub("", normalized)
            digits_only = stripped if stripped.isdigit() else ""
            if CNIC_DIGITS_REGEX.fullmatch(digits_only):
                return (
                    f"{digits_only[:5]}-"
                    f"{digits_only[5:12]}-"
                    f"{digits_only[12]}"
                )
            return stripped
        return cnic

    @api.model
    def _check_cnic_format(self, cnic):
        if cnic and not CNIC_REGEX.fullmatch(cnic):
            raise ValidationError(_(self._CNIC_INVALID_FORMAT_MESSAGE))

    @api.model
    def _check_cnic_uniqueness(self, cnic_values, excluded_ids=None):
        if not cnic_values:
            return
        if len(cnic_values) != len(set(cnic_values)):
            raise ValidationError(_(self._CNIC_DUPLICATE_ERROR_MESSAGE))

        domain = [("cnic", "in", list(set(cnic_values)))]
        if excluded_ids:
            domain.append(("id", "not in", excluded_ids))

        duplicate_count = (
            self.env["res.partner"]
            .sudo()
            .with_context(active_test=False)
            .search_count(domain)
        )
        if duplicate_count:
            raise ValidationError(_(self._CNIC_DUPLICATE_ERROR_MESSAGE))

    @api.model_create_multi
    def create(self, vals_list):
        cnic_values = []
        for vals in vals_list:
            if "cnic" in vals:
                vals["cnic"] = self._normalize_cnic(vals.get("cnic"))
            cnic = vals.get("cnic")
            company = (
                self.env["res.company"].browse(vals.get("company_id"))
                if vals.get("company_id")
                else self.env.company
            )
            if cnic and company.sudo().cnic_validation_enabled:
                self._check_cnic_format(cnic)
            if cnic:
                cnic_values.append(cnic)

        self._check_cnic_uniqueness(cnic_values)

        try:
            return super().create(vals_list)
        except IntegrityError as error:
            if (
                "res_partner_res_partner_cnic_unique" in str(error)
                or "res_partner_cnic_unique" in str(error)
            ):
                raise ValidationError(_(self._CNIC_DUPLICATE_ERROR_MESSAGE)) from error
            raise

    def write(self, vals):
        if "cnic" in vals:
            vals["cnic"] = self._normalize_cnic(vals.get("cnic"))
            cnic = vals.get("cnic")
            if cnic and any(partner._is_cnic_validation_enabled() for partner in self):
                self._check_cnic_format(cnic)
            if cnic and len(self) > 1:
                raise ValidationError(_(self._CNIC_DUPLICATE_ERROR_MESSAGE))
            if cnic:
                self._check_cnic_uniqueness([cnic], excluded_ids=self.ids)

        try:
            return super().write(vals)
        except IntegrityError as error:
            if (
                "res_partner_res_partner_cnic_unique" in str(error)
                or "res_partner_cnic_unique" in str(error)
            ):
                raise ValidationError(_(self._CNIC_DUPLICATE_ERROR_MESSAGE)) from error
            raise

    @api.constrains("cnic")
    def _check_cnic(self):
        partners_with_cnic = self.filtered(
            lambda partner: partner.cnic and partner._is_cnic_validation_enabled()
        )
        if not partners_with_cnic:
            return

        for partner in partners_with_cnic:
            self._check_cnic_format(partner.cnic)

        cnic_values = [partner.cnic for partner in partners_with_cnic]
        self._check_cnic_uniqueness(cnic_values, excluded_ids=self.ids)


class ResCompany(models.Model):
    _inherit = "res.company"

    cnic_field_enabled = fields.Boolean(
        string="Enable CNIC Field",
        default=True,
    )
    cnic_validation_enabled = fields.Boolean(
        string="Enable CNIC Validation",
        default=True,
    )


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    cnic_field_enabled = fields.Boolean(
        related="company_id.cnic_field_enabled",
        readonly=False,
        string="Enable CNIC Field",
    )
    cnic_validation_enabled = fields.Boolean(
        related="company_id.cnic_validation_enabled",
        readonly=False,
        string="Enable CNIC Validation",
    )
