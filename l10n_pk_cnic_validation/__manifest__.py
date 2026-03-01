{
    "summary": "CNIC format validation, auto-formatting & duplicate prevention for Pakistani contacts",
    "description": """
    Enterprise-ready CNIC validation and compliance module for Odoo (Community & Enterprise).

Key features:
- CNIC pattern validation (xxxxx-xxxxxxx-x)
- Auto-format CNIC from 13-digit input
- Validation on Create + Write
- SQL-level duplicate CNIC prevention (fast & production-safe)
- Works in Contacts (res.partner)
- Company Settings toggle to enable/disable validation
- Clean, professional error messages
- Tested on Odoo 17 / 18 / 19
- Migration-ready structure

Built for production Odoo deployments and Odoo Apps Store distribution.
""",

    "version": "18.0.2.0.0",
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
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "application": False,
}
