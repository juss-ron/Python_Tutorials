# 🐍 Types and Variables in Python
# The concept of variables having a fixed type is characteristic of statically-typed languages like Swift. 
# Python, however, is a dynamically-typed language, so its behavior is different.
#
# Here is how the original Swift code and its behavior translate into Python:
#
# Python's Dynamic Typing
# In Python, the variable's type is not fixed to the first assigned value. 
# A variable simply refers to a value, and it can be reassigned to a value of a completely different type at any time.
#

# 1. Initial Assignment
favorite_thing = "Whiskers on kittens" # favorite_thing is currently a string (str)
print(type(favorite_thing))
# Output: <class 'str'>

# 2. Reassignment:
favorite_thing = 42 # favorite_thing is now reassigned to an integer (int)
print(type(favorite_thing))
# Output: <class 'int'>