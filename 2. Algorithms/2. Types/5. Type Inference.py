# 🐍 Type Inference from Assignment in Python
#
# In Python, the concept of type inference works similarly to the example shown, but Python's dynamic typing means the variable itself doesn't have a fixed type; rather, it takes on the type of the value it references at that moment.
#
# An assignment statement has a left side (the variable being assigned to) and a right side (the value that's being assigned):

# left_hand_side = right_hand_side

#The value on the right-hand side will have a type, and the variable on the left-hand side will immediately reference that value and its type.

# Example
# 

string_var = "42"  # string_var is created from a string literal, type is str

another_string = string_var # another_string references the value of string_var

print(type(another_string))
# Output: <class 'str'>


# ❓ The Python Exercise
# Change "42" to 42. What type will another_string have now?
#