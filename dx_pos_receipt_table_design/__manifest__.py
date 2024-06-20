# -*- coding: utf-8 -*-
{
    'name': "POS Receipt Table Design",

    'summary': """
        Change default pos receipt design to table design.""",

    'description': """
        Change default pos receipt design to table design to be more readable and easy to get quantities and price,
        Show customer name on receipt,
        Show receipt number on the top to be more readable.
    """,

    'author': "SADEEM",
    'website': "https://sadeem.cloud",

    'category': 'Point of Sale',
    'version': '17.231119',

    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'dx_pos_receipt_table_design/static/src/xml/OrderReceipt.xml',
        ],
    },
    'images': ['static/description/images/banner.gif'],
    'price': 0.00,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}
