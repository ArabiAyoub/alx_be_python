# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor that initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a Book instance is being deleted."""
        print("Deleting {}".format(self.title))

    def __str__(self):
        """String representation for user-friendly output."""
        return "{} by {}, published in {}".format(self.title, self.author, self.year)

    def __repr__(self):
        """Official string representation that could be used to recreate the object."""
        return "Book('{}', '{}', {})".format(self.title, self.author, self.year)