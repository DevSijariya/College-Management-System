{
    'name': "college_management",
    'version': '18.0',
    'depends': ['base'],
    'author': "Codetrade",
    'category': 'Uncategorized',
    'description': """
    This is the custom school model contain teacher and student information 
    """,
    # data files always loaded at installation
    # xml file and security file are imported in data
    'data': [
        'security/ir.model.access.csv',
        'security/college_access.xml',
        'views/student_views.xml', 
        'views/teacher_views.xml',
        'views/configuration_view.xml',
        'views/courses_views.xml',
        'wizard/teachers_wizard.xml',
    ],

    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'license':'LGPL-3',
    'installable':True,
    'application':True,
}
