# -*- coding: utf-8 -*-
{
    'name': "Prada",

    'summary': """ Prada extra """,

    'description': """
        Prada extra
    """,

    'author': "STECHNOLOGIES",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','mrp_plm','sale','product'],

    'data': [
        'views/mrp_eco_views.xml',
        'views/prada_views.xml',
        'views/product_template_views.xml',
        'wizard/mover_prepedido.xml',
        #'security/prada_security.xml',
    ],
    'license': 'LGPL-3',
}

