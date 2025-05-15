# Distance-Based Shipping Fee

This Odoo module automatically calculates shipping fees based on the customer's distance from your warehouse, using the Google Maps Distance Matrix API.

## Features

- Calculates distance and travel time from your warehouse to the customer.
- Adds two invoice or sales order lines:
  - **Shipping Fee per KM**
  - **Shipping Fee per Hour**
- Manual override when API fails (e.g. customer picks up order).
- Fully configurable rates in the **Settings > General Settings** menu.

## Setup

1. Install the module.
2. Navigate to Settings > General Settings and configure:
   - Price per KM
   - Price per Hour
   - Google Maps API Key
3. On a Sales Order or Quotation, click **"Add Shipping Fee"** to calculate and insert the shipping lines.

## Requirements

- A valid Google Maps Distance Matrix API Key with billing enabled.

## License

LGPL-3
