# Creating an Instance in Python

    # So far, you’ve created almost every object (instance) by typing a literal value directly into code. 
    # You may have also used built-in functions like time.time() to get a value:
#

import time

literal_string = "Howdy!"
literal_bool = False
literal_int = 84

right_now_timestamp = time.time()  # This returns a float representing seconds since the epoch

print(right_now_timestamp)

# When you need to create a new object using a type name (like a built-in type or a custom class), you often use parentheses () immediately after the name:

import datetime

# This creates a datetime object representing the current date and time
right_now = datetime.datetime.now()

print(right_now)

# The use of datetime.datetime.now() looks like a function call, but creating a new list, for example, is done directly on the type name:
empty_list = list()

# Initializers in Python
    # In Python, the process of creating a new instance is handled by the constructor pattern. 
    # When you call a type (or class) followed by parentheses, 
    # Python executes special methods behind the scenes to create and set up the new object.

    # This is how you create a new, default instance of a basic built-in type:
#

# Creates an empty string instance
empty_string = str() 

# Creates a False boolean instance (only False is allowed for Bool())
false_bool = bool() 

# Creates an integer instance with the value 0
zero = int() 

# Creates an empty list instance
empty_list = list()

# Initializers with Arguments
    # You'll often want to provide more information when you create an instance. 
    # Many types have constructors that accept arguments to customize the instance during creation.

    # For example, the int() type can take a string or float as an argument to initialize its value:
#

# Initializes 'my_int' to the integer 123
my_int = int("123")

# Initializes 'my_list' with the characters 'H', 'i'
my_list = list("Hi")

# Initializers vs. Regular Functions

    # When comparing calling a type to create an instance with calling a regular function:

    # Feature: Type Constructor (e.g., list(), str())

        # Name Used: The name of the Type (list, str).

        # Purpose: Creates and returns a new instance of the specified type (an object).

        # Returns: A new object.

    # Feature: Regular Function (e.g., print(), len())

        # Name Used: A function name (often lowercase, like print).

        # Purpose: Executes a defined block of code (like calculating a value or printing to the console).

        # Returns: A value determined by the function (or None).
