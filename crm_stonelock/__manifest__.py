{
    'name': "Stonelock Opportunity Aging",
    'summary': "Stonelock opportunity aging",
    'description': """
    task id: 2308586
    custom field for opportuunity aging""",
    'author': 'Odoo',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '15.0.1.0',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        'views/inherit_crm_form.xml'
    ],
    'application': False,
}