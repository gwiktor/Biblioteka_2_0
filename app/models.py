  
from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    info = db.Column(db.String(50))
    books_auth = db.relationship("Book", backref="author", lazy="dynamic")

    def __str__(self):
        return f"<Author: {self.name}>"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, index=True)
    description = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    available = db.relationship("Off_Shelf", backref="book", lazy="dynamic")

    def __str__(self):
        return f"<Book: {self.id} {self.title[:50]}...>"


class Off_Shelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Off_Shelf: {self.id}...>"