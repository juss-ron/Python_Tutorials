# 🐍 Type Hints (Annotation) in Python
# In Python, the mechanism used to explicitly indicate a variable's expected type is called Type Hinting (or Type Annotation), which was introduced in PEP 484.
#
# While Python is dynamically typed and doesn't require type hints to run, they are crucial for:
# documentation, 
# helping developers understand the code, 
# and enabling static type checkers (like Mypy) to catch potential errors before the program runs.
#
# Case 1: Python's Inference on Empty Variables
# The Swift example highlights an error when declaring a constant without an initial value, as the type cannot be inferred.
#
# In Python, trying to declare a variable without an initial assignment simply isn't valid syntax, as variables are created upon assignment:

# Uncommenting this line in Python would result in a SyntaxError
# The interpreter expects an assignment statement (e.g., mystery_constant = None)
# mystery_constant

# Case 2: Explicit Type Hinting
# There are cases when you want to make the type explicit, especially when the inferred type might be confusing or for better code clarity.
#
# In Python, a type hint is added after the variable name using a colon (:), followed by the type name:
#

# 1. Explicitly make 20 a float using a type hint
annotated_float: float = 20
print(f"Type of annotated_float: {type(annotated_float)}")
# Output: Type of annotated_float: <class 'float'>

# 2. Python infers this as a float because of the decimal point
inferred_float = 0.5
print(f"Type of inferred_float: {type(inferred_float)}")
# Output: Type of inferred_float: <class 'float'>

# 3. Performing the calculation
result = inferred_float * annotated_float
print(f"Type of result: {type(result)}")
# Output: Type of result: <class 'float'>