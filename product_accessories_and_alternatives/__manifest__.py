# -*- coding: utf-8 -*-
{
    'name': 'Product Accessories & Alternatives',
    'version': '1.1',
    'category': 'Sales',
    'summary': 'Manage accessories and alternative without E-Commerce',
    'description': """
The app aims to add accessories and alternatives to products. Odoo standard package let such functionality but only with E-shop installed.
* Manage accessories and alternatives through the smart buttons. Comfortable and clear. Counters in real time
* The app is anyway compatible with 'website_sale'. It means that if you installed the latter, the data would be kept saved and may be used in E-shop
""",
    'auto_install': False,
    'author': 'IT Libertas',
    'website': 'https://odootools.com',
    'depends': [
        'product',
    ],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'wizard/product_accessories_wizard.xml',
        'wizard/product_alternatives_wizard.xml',
        'views/product_template.xml',
    ],
    'qweb': [

    ],
    'js': [

    ],
    'demo': [

    ],
    'test': [

    ],
    'license': 'Other proprietary',
    'images': [
        'static/description/main.png',
    ],
    'update_xml': [

    ],
    'application': True,
    'installable': True,
    'private_category': False,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'post_load': 'post_load',
    'uninstall_hook': 'uninstall_hook',
    'external_dependencies': {
    },

}
