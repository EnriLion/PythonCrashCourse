# A class instance is a defined set of properties called an object

# In Python built-in classes are named in lower case


class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None
        # self.__discount = 0.10

        # we can't expect to provide specific info on qualities(title,author_name...)

        # we can use a method called __repr__ to do this(the above)

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self__discount)
        return self.__price

    def __repr__(self):
        """This method could return the main __init_ method"""
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"
        # return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price:{self.price}"


# book1 = Book('Book 1', 12, 'Author 1', 120)
# book2 = Book('Book 2', 18, 'Author 2', 220)
# book3 = Book('Book 3', 28, 'Author 3', 320)

single_book = Book('Two States', 1, 'Chetan Bhagat', 200)

bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)
bulk_books.set_discount(0.20)

# print(book1.title)
# print(book1.quantity)
# print(book1.author)
# print(book1.price)
# print(book1.__discount)

print(single_book.get_price())
print(bulk_books.get_price())
print(single_book)
print(bulk_books)


# The term self  in the attributes refers to instances(objects).

# output of each object without the return:

# <__main__.Book object at 0x7fe06efd6860>
# <__main__.Book object at 0x7fe06efd6800>
# <__main__.Book object at 0x7fe06efd67a0>
