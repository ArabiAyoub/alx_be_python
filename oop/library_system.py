# library_system.py

# class Book:
class Book(object):  # Inherits from object to be a new-style class
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "Book: {} by {}".format(self.title, self.author)

# class EBook:
class EBook(Book):
    def __init__(self, title, author, file_size):
        super(EBook, self).__init__(title, author)  # Ensure this line is exactly as needed
        self.file_size = file_size

    def __str__(self):
        return "EBook: {} by {}, File Size: {}KB".format(self.title, self.author, self.file_size)

# class PrintBook:
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super(PrintBook, self).__init__(title, author)  # Ensure this line is exactly as needed
        self.page_count = page_count

    def __str__(self):
        return "PrintBook: {} by {}, Page Count: {}".format(self.title, self.author, self.page_count)

# class Library:
class Library(object):  # Inherits from object
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)