from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Livro'


    name = fields.Char(string='Titulo', required=True)
    author = fields.Char(string='Author')
    published_date = fields.Date(string='Data de Publicação')


    def get_books_by_author(self, author_name):
        return self.search([('author', '=', author_name)])
    

    def create_book(self, vals):
        """
            create a new book
            :param vals: dictionary with book date
        """

        return self.create(vals)
    
    def update_book(self, book_id, vals):
        """
            update an existente book
            :param book_id: book id
            :param vals: new date of dictionary
        """
        book = self.browse(book_id)
        if book.exists():
            book.write(vals)

        return book
    
    def delete_book(self, book_id):
        """
            delete a new existente book
            :param book_id
        """

        book = self.brwose(book_id)
        if book.exists():
            book.unlink()
            