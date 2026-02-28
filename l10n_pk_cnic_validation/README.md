# Pakistan CNIC Validation for Contacts

Pakistan CNIC Validation for Contacts is a commercial-grade Odoo 18 module designed for organizations operating in Pakistan that need accurate identity data on contact records. It adds a dedicated CNIC field to contacts, enforces consistent formatting, prevents duplicate entries, and provides per-company configuration controls to fit real multi-company deployments.

## Key Features

- Adds a dedicated CNIC field on contacts with enterprise-ready behavior
- Auto-formats CNIC input from 13 digits into `12345-1234567-1`
- Enforces strict CNIC format validation with professional user feedback
- Prevents duplicate CNIC entries across all partners
- Supports multi-company deployments with per-company settings
- Allows administrators to enable/disable CNIC field visibility
- Allows administrators to enable/disable CNIC validation rules
- Includes SQL uniqueness and indexed CNIC column for large databases

## Configuration

1. Go to **Settings → General Settings**.
2. Open the **CNIC Validation (Pakistan)** section.
3. Configure per company:
   - **Enable CNIC Field**: Shows or hides the CNIC field on contacts.
   - **Enable CNIC Validation**: Enables or bypasses CNIC format enforcement.
4. Switch company and configure the same options independently as needed.

## How It Works

- **Backend validation**: Python constraints validate CNIC format using strict regex and raise clear validation errors.
- **Auto-format logic**: CNIC values entered as raw digits are normalized in `create()` and `write()` before validation.
- **SQL constraint**: Database-level unique constraint protects data integrity and prevents duplicate CNIC values.

## Technical Details

- Fully compatible with **Odoo 18 Enterprise**
- Multi-company safe configuration through `res.config.settings` and company-level fields
- OWL-compatible JavaScript enhancement for frontend CNIC formatting UX
- Indexed CNIC column for fast lookups in high-volume environments
- Migration-ready structure for future version upgrades

## Installation

1. Copy the module folder to your custom addons path.
2. Restart Odoo service.
3. Update Apps List from Apps menu.
4. Search and install **Pakistan CNIC Validation for Contacts**.

## Use Cases

- Pakistani SMEs managing customer and vendor master data
- Accounting and tax firms requiring clean CNIC records for compliance workflows
- ERP implementation partners deploying standardized localization controls

## Compatibility

- Odoo 18 Enterprise (supported)
- Odoo Community: core behavior may work, but Enterprise layout and UX are optimized for Enterprise deployments

## Support

For technical support, implementation guidance, and customization requests, contact: **support@example.com**.

## Author

**Your Company Name**  
Enterprise Odoo Solutions & Localization Services
