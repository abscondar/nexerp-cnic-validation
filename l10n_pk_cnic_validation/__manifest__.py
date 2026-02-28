{
    "name": "Pakistan CNIC Validation",
    "summary": "Per-company CNIC formatting and validation for Pakistani contacts",
    "description": """
Commercial-grade CNIC validation module for Odoo 18 Enterprise.

Key features:
- Automatic CNIC formatting for 13-digit input.
- Per-company control to enable/disable CNIC field visibility.
- Per-company control to enable/disable strict CNIC validation.
- Global duplicate prevention with SQL and ORM safeguards.
- Optimized indexing and migration-ready structure for long-term maintenance.

Designed for production environments and Odoo Apps Store distribution.
""",
    "version": "17.0.2.0.0",
    "category": "Localization",
    "license": "LGPL-3",
    "author": "Your Company",
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
