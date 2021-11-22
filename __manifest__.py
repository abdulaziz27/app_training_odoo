# -*- coding: utf-8 -*-
{
    'name': "Training Odoo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modul ini merupakan percobaan 1
    """,

    'author': "Umar Fakhry",
    'website': "instagram.com/umarfakhry",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'report/report_view.xml',
        'report/print_sesi.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/partner.xml',
        'views/templates.xml',
        'wizard/wizard_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
}
