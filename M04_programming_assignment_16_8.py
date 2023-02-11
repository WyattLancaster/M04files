# m04 - Programming Assignment: Modules and Databases 16.8
# author: WJL
# created: 2022-02-11
# program imports info from sqlalchemy and predefined info and creates a class "Book" with title, author, and year attributes it then connects to the database to retrieve the pre entered books and then prints them alphabetically

# Import from sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Creating the "Base" variable
Base = declarative_base()

# Creating the "Book" object
class Book(Base):
    __tablename__ = 'books'
    title = Column(String, primary_key=True)
    author = Column(String)
    year = Column(Integer)

# Connect to the database
engine = create_engine('sqlite:///books.db')
Session = sessionmaker(bind=engine)
session = Session()

# Select and print the title column in alphabetical order
books = session.query(Book).order_by(Book.title)
for book in books:
    print(book.title)

# Close the connection
session.close()