{
    'name': "Kororo Survey Monkey",
    'version': '1.0.0',
    'depends': ['base'],
    'author': "Kororo",
    'website': 'https://kororo.co',
    'category': 'Kororo/survey',
    'description': """
    Kororo Survey Monkey Connector
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'auto_install': False,
    'maintainer': 'safrizal@kororo.co',
    'license': 'OEEL-1',
}