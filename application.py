# m04 - Lab Case study
# author: WJL
# created: 2022-02-12
# program creates a CRUD API for books which all have attributes that are defined

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Define the Book model with fields id, book_name, author, and publisher
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(120), nullable=False)

# Define the string representation of the Book model
    def __repr__(self):
        return f"{self.id} - {self.book_name} - {self.author} - {self.publisher}"

# The root endpoint returns the string 'Hello!'
@app.route('/')
def index():
    return 'Hello!'

# The /books endpoint returns a list of all books in the database
@app.route('/books')
def get_books():
# Query all books from the database
    books = Book.query.all()

# Prepare the output list with dictionaries containing book data
    output = []
    for book in books:
        book_data = {'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)

# Return the output list as a dictionary with the key 'books'
    return {"books": output}

# The /books/<id> endpoint returns a single book with the specified id
@app.route('/books/<id>')
def get_book(id):
# Query the book with the specified id or return a 404 error
    book = Book.query.get_or_404(id)

# Return the book data as a dictionary
    return {'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}

# The /books endpoint with the POST method adds a new book to the database
@app.route('/books', methods=['POST'])
def add_book():
# Create a new book from the request data and add it to the database
    book = Book(id=request.json['id'], book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()

# Return the id of the added book
    return {'id': book.id}

# The /books/<id> endpoint with the DELETE method deletes the book with the specified id from the database
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
# Query the book with the specified id
    book = Book.query.get(id)

# Return an error if the book was not found
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet"}