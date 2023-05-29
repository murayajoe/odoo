# -*- coding: utf-8 -*-
{
    'name': "om_odoo_inheritance",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "Muraya",
    'website': "http://www.anqad.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': -101,

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/templates.xml',
        'views/account_move_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
