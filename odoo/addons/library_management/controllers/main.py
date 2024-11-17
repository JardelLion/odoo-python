import json
from odoo import http
from odoo.http import request
from datetime import datetime

class LibraryController(http.Controller):
    @http.route('/api/books', type='http', auth='public', methods=['GET'], csrf=False)
    def get_books(self, **kwargs):
        # Buscar todos os livros do modelo library.book
        books = request.env['library.book'].sudo().search([])

        # Estruturar os dados para retorno
        books_data = [
            {
                'id': book.id,
                'title': book.name,
                'author': book.author,
                'published_date': book.published_date.strftime('%Y-%m-%d') if book.published_date else None
            }
            for book in books
        ]
        
        # Retornar os dados em formato JSON
        return request.make_response(
            json.dumps({'books': books_data}),
            headers=[('Content-Type', 'application/json')],
            status=200
        )
