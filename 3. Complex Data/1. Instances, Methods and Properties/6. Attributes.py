# Attributes

    # At the start of this lesson, you thought about different types like "City" and "Car." 
    # You can imagine each instance of a city having a different name or each instance of a car having its own mileage.

    # Similarly, in Python, each instance has one or more pieces of associated information. 
    # These values are known as attributes.

    # It’s often useful to know the specific characteristics of an object. 
    # While Python strings often use methods for these checks, other types—like complex numbers or custom objects—use attributes to store data.

    # Defining an Attribute
        # An attribute is like a variable that is "attached" to an instance. 
        # Just as a method is a function built into each instance of a type, an attribute is a value built into each instance of a type.

    # In Python, attributes are accessed using the dot notation (.), just like methods, but without the parentheses at the end.

    # How to Access Attributes
        # Attributes are called by using a period (.) after the instance, followed by the attribute name:
#

# A complex number instance has 'real' and 'imag' attributes
my_number = 3 + 5j

print(my_number.real)
# Output: 3.0

print(my_number)
# Output: 5.0

#
    # Notice that there are no parentheses () after real or imag. 
    # This is because we are accessing a value stored on the object, not asking the object to perform an action.

# Attributes and Type Safety
    # You can’t use an attribute without an instance. 
    # You can't just type .real into your code; Python needs to know which object's real part you are looking for.

    # You can only use attributes that are part of the type of the instance.

    # Experiment: Try to run the following code in a Python environment:
#

greeting = "Hello"
# print(greeting.real)

#
    # The error this time would be AttributeError: 'str' object has no attribute 'real'. 
    # A string is a sequence of characters; it doesn't have a "real number" attribute like a complex number does.

    # Note: 
        # The built-in types you’ve worked with so far (like int and str) rely mostly on methods because the information they store is very simple.
        # As you create more complicated objects later, you will see attributes used much more frequently to store data like names, ages, or coordinates.