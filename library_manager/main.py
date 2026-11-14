# main.py
from models import Book, Member,Magazine,DVD  # TODO: also import Magazine, DVD

book = Book("Python 101", 1, "A. Rao")
# TODO: create one Magazine and one DVD
magazine = Magazine("Sports Center", 2, "Some Sports Man",1234)
dvd = DVD("RRR",3,"S.S.R",240)
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)
# 2. TODO: trigger the borrow-limit error and the not-borrowed error, catching each
# 2a. Borrow-limit error: Bob's max_items is 1
try:
    bob.borrow(magazine)   # works, Bob now holds 1 item
    bob.borrow(dvd)        # fails: limit reached
except ValueError as e:
    print("Could not borrow:", e)

# 2b. Not-borrowed error: Alice never borrowed the DVD
try:
    alice.return_item(dvd)
except ValueError as e:
    print("Could not return:", e)

# 3. Polymorphism: one loop, no type checks
items = [book,magazine,dvd]  # TODO: add the magazine and the DVD

for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))
# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)
