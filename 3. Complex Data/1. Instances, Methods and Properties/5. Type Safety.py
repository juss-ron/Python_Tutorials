# Methods and Type Safety

# Type safety still applies when you're using instance methods in Python. The method .startswith() is a string instance method, so you can't use it without an instance of the str type.

# 1. Calling a Method Without an Instance
    # If you try to call a method directly without an object to act upon, Python won't know where to find that function.

    # Experiment: 
        # Try to run the following line:
#

# print(startswith("It was"))

#
    # The error you would see is likely NameError: name 'startswith' is not defined. 
    # This means Python cannot find a standalone function named startswith that can be called on its own. 
    # Instance methods must be called using the dot operator (.) on an instance.

# 2. Calling a Method on the Wrong Type
    # You also cannot use an instance method on an instance of the wrong type. 
    # You can only use methods that are part of, or members of, a particular type (or class).

    # Experiment: 
        # Try to run the following code:

number = 42
# print(number.startswith("It was"))

