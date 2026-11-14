Ques:> Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?
Ans-> LibraryItem is abstract because the class inherits "ABC" class and has atleast one abstract method.
If DVD forgets to write late_fee(), there will be an error while creating DVD object. 
Error: TypeError: Can't instantiate abstract class DVD with abstract method late_fee

Ques:> What happens when you read item.__available from outside the class, and why do we use is_available() instead?
Ans:> Reading item.__available from outside the class gives an AttributeError, because Python renames double-underscore attributes inside the class and the original name is not available outside. We use is_available() so the value is private and can only be read through a method. Other code cannot change it directly. It changes only through mark_borrowed() and mark_returned().

Ques:> What is the difference between LibraryItem.total_items and self.title?
Ans:>  LibraryItem.total_items is a class attribute while self.title is an instance attribute