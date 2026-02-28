{
    "name": "Pakistan CNIC Validation for Odoo",
    "summary": "Enterprise-grade CNIC format validation, auto-formatting and duplicate prevention for Pakistani contacts.",
    "description": """Enterprise-ready CNIC validation and compliance module for Odoo.

✔ Automatic CNIC formatting (xxxxx-xxxxxxx-x)
✔ Strict validation on create and write
✔ SQL-level duplicate prevention
✔ Optimized indexing
✔ Company-level enable/disable toggle
✔ Multi-version tested (17, 18, 19)
✔ Migration-ready architecture

Built for production environments and Odoo Apps Store distribution.
""",
    "version": "17.0.2.0.0",
    "category": "Localization",
    "license": "LGPL-3",
    "author": "NexERP Labs",
    "website": "https://github.com/abscondar",
    "price": 49.0,
    "currency": "USD",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "l10n_pk_cnic_validation/static/src/js/cnic_format.js",
        ],
    },
    "installable": True,
    "application": False,
}
