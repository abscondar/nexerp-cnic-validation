{
    "name": "Pakistan CNIC Validation & Duplicate Protection",
    "summary": "CNIC format validation, auto-formatting and duplicate control for Pakistani contacts",
    "description": """
Professional CNIC validation module for Pakistani businesses using Odoo.

✔ Enforces correct CNIC format (xxxxx-xxxxxxx-x)
✔ Automatic formatting for 13-digit input
✔ SQL-level duplicate protection
✔ Validation on create and write
✔ Company-level control to enable/disable validation
✔ Optimized and migration-ready architecture

Compatible with Odoo 17, 18 and 19.
""",
    "version": "19.0.2.0.0",
    "category": "Contacts",
    "license": "LGPL-3",
    "author": "NexERP Labs",
    "website": "https://github.com/abscondar",
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
