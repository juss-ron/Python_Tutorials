# Errors

    # When the Python interpreter (or environment) finds an error in your code, 
    # it stops running the program and reports the issue. This is how you learn where problems are located.

# Error Type 1: Syntax Errors / Name Errors

    # The line of code below has an intentional spelling mistake, which Python 
    # interprets as a name it doesn't recognize. When you run this, you will see 
    # a traceback that identifies the line and the type of error: NameError.
    # NameError means you tried to use a variable or function name that was not defined.

    # 👇 Notice that the line of code below will cause an error when you run the script.
    # The error message will say something like "NameError: name 'primt' is not defined."
    # This is how you identify where a problem is.
#

primt("Hello, World")

# Fix the error: 
    # Fix the syntax error by changing 'primt' to the correct function name: 'print'




# Another example of an errror is "Division by 0"
# You can’t divide by zero in math class, and a computer can’t divide by zero either.

1000 / 0

# Change the 0 to another number to fix the error.








print("Hello, World")


# Error Type 2: Runtime Errors (e.g., Division by Zero)

# Another example of a fundamental runtime error is "Division by 0".
# You can’t divide by zero in math class, and a computer can’t divide by zero either.
# Python throws a specific error for this problem: ZeroDivisionError.

# print(1000 / 0)

# Fix the error:
# Change the 0 to another number to fix the error.

print(1000 / 5)
# Expected result: 200.0


# Exercise

# Practice identifying and fixing errors by uncommenting the lines below one at a time.
# Read the error message in the console carefully to understand the problem, 
# then fix the line before moving on to the next.

# 1. Syntax Error: Missing necessary punctuation
# print("This line is missing its closing parenthesis" 

# 2. Type Error: Attempting an invalid operation
# print("2" + 2) 

# 3. Name Error: Unknown variable
# my_variable = 10
# print(my_vairable)