# -*- coding: utf-8 -*-
{
    'name': "tessract",

    'summary': """
        Adds custom fields (GST Number, Contact Number, Client Name) to the customer form.""",

    'description': """
       This module extends the customer form (res.partner) by adding three new fields:
        - GST Number
        - Contact Number
        - Client Name
            """,

    'author': "Mayank",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '1.0',
    'category': 'Custom',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','account','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/report_sales_action.xml',
        'report/report_sales_document.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
}
