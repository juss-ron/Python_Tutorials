# 🐍 Passing More Values in Python
    # To make a Python function accept more than one value, you simply list the parameters inside the parentheses of the function definition, separating them with a comma.

# 📝 Defining the Function
    # The function is defined using the def keyword, and the parameters are listed, often with type hints for clarity:
#

def hello(first_name: str, last_name: str):
    """Greets a person using their first and last name."""
    
    # Inside the function, you can access the values using f-strings (formatted strings)
    # for cleaner concatenation.
    print(f"Hello {first_name} {last_name}")


# 🧐 Breaking Down the Parameters
    # You can picture the parameter list clearly as separate elements:

        # first_name: str

        # last_name: str

    # Both first_name and last_name act as local variables inside the function body, holding the string values passed in when the function is called.

# 📞 Calling the Function
    # When calling the function in Python, you pass the arguments in the order they were defined. 
    # Unlike the default Swift call format, you do not typically include the parameter names (firstName:, lastName:) when passing arguments positionally.


hello("Johnny", "Appleseed")
# Output: Hello Johnny Appleseed

hello("John", "Snow")
# Output: Hello John Snow

# Keyword Arguments (Optional)
    # Although not strictly required in this basic example, 
    # Python allows you to call the function using keyword arguments, which explicitly name the parameter, 
    # making the call clearer (similar to the Swift syntax):

# Calling the function using keyword arguments
hello(last_name="Appleseed", first_name="Johnny") # Order doesn't matter here
# Output: Hello Johnny Appleseed

# This flexibility is a hallmark of Python functions!

# Exercise:
    # Call the function a few more times using different inputs


