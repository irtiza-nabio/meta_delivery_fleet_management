{
    'name': 'Delivery Fleet Management',
    'version': '1.0',
    'summary': 'Manage internal and external deliveries with fleet integration and tracking',
    'description': """
        This module extends the stock picking process by introducing:
        - Internal and external delivery types
        - Vehicle, driver, and helper assignments
        - Third-party provider tracking for external deliveries
        - Start/End buttons for delivery tracking
        - Field visibility and access control based on delivery state
    """,
    'category': 'Warehouse',
    'author': 'Metamorphosis',
    'license': 'LGPL-3',
    "depends": [
        "base", "contacts", "stock", "fleet"
    ],
    "data": [
        'views/res_partner_search.xml',
        'views/stock_picking_search.xml',
        "views/res_partner_views.xml",
        "views/stock_picking_views.xml",
        "security/ir.model.access.csv"
    ],
    "installable": True,
    "application": False
}