# Methods in Python

    # Methods in Python are essentially functions that are associated with an object (instance) of a specific type (class). 
    # They are used to perform actions or calculations that pertain to that specific object's data. 
    # The concepts of instance methods and methods are the same in Python.

    # Here are two string instances (objects) in Python:
#

introduction = "It was a dark and stormy night"
alternate_introduction = "Once upon a time"

#
    # It’s often useful to know if a string begins with another string. The method .startswith() answers this question.

    # In Python, the method is conceptually defined to take the prefix string as an argument and return a boolean value:
#

# Conceptual Python definition (for illustration)
# def startswith(prefix: str) -> bool:
#    ...

#
    # The method .startswith() takes a string argument, which is the prefix you want to test, and returns a bool (True or False).

# Calling a Method
    # Instance methods are called by using a dot (.) after the instance name, followed by the method call:
#

# Calling the method on the 'introduction' string instance
print(introduction.startswith("It was"))
# Output: True

print(introduction.startswith("It wasn't"))
# Output: False

# Calling the method on the 'alternate_introduction' string instance
print(alternate_introduction.startswith("It was"))
# Output: False

print(alternate_introduction.startswith("Once"))
# Output: True

#
    # This is known as calling a method on the instance. You called .startswith() on introduction and alternate_introduction.

    # The method .startswith() returns different answers depending on the argument you provide and the value of the instance it is called on. 
    # You can call this method on any instance of the str type, and you will get the correct answer because every string object knows how to figure out the answer for itself. 
    # Every instance of str has this built-in functionality ready to be used.