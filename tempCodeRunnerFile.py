
class Library:

    # Class Variable
    library_name = "Central Library"

    # Constructor
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    # Instance Method
    def display_book(self):
        print("Book Name :", self.book_name)
        print("Author    :", self.author)
        print("Price     :", self.price)

    # Instance Method
    def update_price(self, new_price):
        self.price = new_price
        print("Price Updated Successfully")

    # Class Method
    @classmethod
    def get_library_name(cls):
        return cls.library_name

    # Static Method
    @staticmethod
    def discount(price, percent):
        return price - (price * percent / 100)


# Create Objects
b1 = Library("Python Programming", "Guido van Rossum", 1000)
b2 = Library("SQL Basics", "John Smith", 800)

# Display Book Details
b1.display_book()
print("-" * 30)

b2.display_book()
print("-" * 30)

# Update Price
b1.update_price(1200)

print("\nUpdated Book Details")
b1.display_book()

# Class Method
print("\nLibrary Name:", Library.get_library_name())

# Static Method
discount_price = Library.discount(1200, 10)
print("Price After 10% Discount:", discount_price)