class Book: 
    # we can also put variables and these become class properties. 
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name 
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}gr"

    @classmethod 
    def hardcover(clas, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100) 



#for print the type =, we have to in to the class book. 
print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)

print(book.name)