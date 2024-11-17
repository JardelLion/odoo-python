{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Jardel Elias Bernardo',
    'description': "Modulo para gerenciar livros",
    'depends': ['base'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/book_view.xml',  # Arquivo XML que contém a definição de views
    ],
    
    'installable': True,
    'application': True,
}
