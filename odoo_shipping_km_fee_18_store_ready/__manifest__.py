{
    "name": "Distance-Based Shipping Fee",
    "summary": "Calculate and add delivery cost based on distance and travel time",
    "version": "18.0.1.0.0",
    "author": "Your Name",
    "maintainer": "Your Name",
    "website": "https://yourcompany.com",
    "category": "Sales/Delivery",
    "license": "LGPL-3",
    "depends": ["account", "sale", "sale_renting"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_config_settings_views.xml",
        "views/sale_order_views.xml",
        "views/shipping_manual_entry_wizard_view.xml"
    ],
    "installable": True,
    "application": False,
    "price": 0.0,
    "currency": "EUR"
}
