# 🐍 From Specific to General in Python

    # You're looking to convert the Swift concept of moving from a specific function to a general function that accepts a parameter (argument) into Python.

    # In Python, this is achieved using a function parameter inside the parentheses of the function definition.

    # 1. The Specific Function
        # In Python, a function that performs a specific, hardcoded action looks like this:
#

def hello_johnny():
    name = "Johnny"
    print("Hello " + name)

hello_johnny()
# Output: Hello Johnny

#
    # Just like in the Swift example, the function hello_johnny() is too specific. 
    # If you wanted to greet someone else, you'd have to write a brand new function, which is inefficient.
#

# 2. The General Function with a Parameter

    # Instead of writing multiple specific functions, you write one general function that takes a parameter. 
    # This parameter acts as a placeholder for the information the function needs (the name), which will be supplied later when the function is called.

    # 📝 Declaration (Definition)
        # The parameter is added inside the parentheses () when you define the function using the def keyword. 
        # For clarity, we'll also use a type hint to specify the expected type, similar to the Swift type annotation.
#

def hello(name: str):
    # 'name' is a parameter that acts like a variable inside the function body
    print("Hello " + name)

#
    # The function hello now has a parameter, called name, which is expected to be a str (String).

    # 📞 Calling the Function (Passing an Argument)
    # Later, when you call the function, you provide the actual value—called the argument—for the name parameter.
#

hello("Maria")
# Output: Hello Maria

hello("Vikram")
# Output: Hello Vikram

# Experiment
    # Call the function below

