{
    'name': 'Invoice extends',
    'version': '16.0.0.5',
    'category': 'Tools',
    'license': 'OPL-1',
    'summary': 'Easily Customizable Report Template for Invoice',
    'description': """
		Customize report, customize pdf report
		
    """,
    'license': 'OPL-1',
    'author': 'GlobalCare',
    'depends': ['base', 'account', 'sale', 'sale_management'],
    'data': [
        "views/res_company.xml",
        "invoice_report/fency_report_invoice.xml"
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
  }
