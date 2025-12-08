# Methods vs. Attributes: When to use ()

    # In Python, the biggest visual difference between a method and an attribute is the set of parentheses () at the end. 
    # It can be helpful to think of it this way:

    # Attributes are like nouns: They describe what an object is or has (e.g., color, size, real part).

    # Methods are like verbs: They describe what an object can do (e.g., convert to uppercase, start with a prefix).

    # Differences

        # Attribute

            # Syntax: object.attribute

            # What it represents: A piece of data or a state.

            # Does it calculate?: No, it just retrieves a stored value.

            # Example: my_number.real

        # Attribute

            # Syntax: object.method()

            # What it represents: A behavior or action.

            # Does it calculate?: Yes, it often performs logic or a search.

            # Example: my_string.startswith("A")

    # Practice: Identifying the Difference
    # Look at these examples to see how Python treats them differently based on whether they are providing data or performing an action:
#

# Create a string instance
text = "python programming"

# 1. ACTION (Method)
# We want the string to DO something: convert to uppercase.
# We use parentheses because it's an action.
print(text.upper()) 

# 2. DATA (Attribute)
# Imagine a coordinate point object (from a library like 'collections')
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
my_point = Point(10, 20)

# We want to get the DATA: the x-coordinate.
# We don't use parentheses because it's a stored value.
print(my_point.x)

# Using dir() to Inspect Types
    # When you pass an object into dir(), Python returns a list of everything that instance "knows" how to do (methods) and "knows" about itself (attributes).
#

text = "Hello"
print(dir(text))

# If you run this, you will see a large list. It includes familiar methods like startswith, upper, and lower.

# Understanding "Dunder" Methods
    # You will notice many items in that list that start and end with double underscores, like __add__ or __len__. 
    # These are called Double Underscore methods, or "Dunder" methods.

    # These are special methods that Python uses behind the scenes. For example:

    # When you use + to add two numbers, Python is actually calling __add__.

    # When you use len(my_string), Python is calling __len__.

# Quick Tip: The help() Function
    # If dir() tells you what is available, the help() function tells you how to use it. 
    # If you aren't sure if something is a method (requiring ()) or an attribute, you can ask Python directly:
#

# This will show you the documentation for the 'startswith' method
help(text.startswith)

# The output will show you that it is a "method" and tell you exactly what arguments it expects.

# Tools for Discovery
    # Function: type()

        # What it does: Tells you the name of the type/class.

        # Example: type("Hi") -> <class 'str'>

    # Function: dir()

        # What it does: Lists all available attributes and methods.

        # Example: dir(str)

    # Function: help()

        # What it does: Provides the "instruction manual" for a method.

        # Example: help(str.upper)