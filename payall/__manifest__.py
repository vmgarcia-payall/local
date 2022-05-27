# -*- coding: utf-8 -*-
{
    'name': "payall",

    'summary': """
        Modulo implementado para la gestion de pagos y recargas""",

    'description': """
        Modulo implementado para la gestion de pagos y recargas
    """,

    'author': "Payall",
    'website': 'https://payall.com.ve/',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/chart_data.xml',
        'data/account.account.template.csv',
        'data/chart_post_data.xml',
        'data/chart_template_data.xml',
        'data/res_partner.xml',
        'views/currencies.xml',
        'views/rates.xml',
        'views/rates_type.xml',
        'views/account_move_inherit_view.xml',
        'views/res_partner_inherit.xml',
        'views/res_country_state_view.xml',
        'views/res_state_municipio_view.xml',
        'views/res_municipio_parroquia_view.xml',
        'views/res_parroquia_urbanizacion_view.xml',
        'data/res.country.state.csv',
        'data/res.state.municipio.csv',
        'data/res.municipio.parroquia.csv',
        'data/res.parroquia.urbanizacion.csv'

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
