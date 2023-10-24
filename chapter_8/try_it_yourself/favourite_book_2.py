# 8-2. Favourite Book:  Write a funciton called favourite_book() that accepts one
#                       parameter, title. The function should print a message,
#                       such as, One of my favourite books is Alice in Wonderland.
#                       Call the function, making sure to include a book title
#                       as an argument in the function call.


def favourite_book(book):
    print(f"One of my favourite books is {book.title()}.")

favourite_book("Alice in Wonderland")