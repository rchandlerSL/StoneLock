# -- coding: utf-8 --
{
    'name': "Stonelock Opportunity Aging",
    'summary': "Stonelock opportunity aging",
    'description': """
    task id: 2308586
    custom field for opportuunity aging""",
    'author': 'Odoo',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        'views/inherit_crm_form.xml'
    ],
    'application': False,
}