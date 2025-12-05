# 👕 Matching Names and Types in Python
    # The analogy about your favorite shirt and a banana illustrates a core concept in programming: Type Consistency.

    # If you take a moment to imagine your favorite shirt, it's probably not a banana. That doesn't make sense. 
    # A banana is not a shirt.

    # On the other hand, if you think about your favorite fruit, whether it's a banana, an apple, or something else, it's almost certainly some kind of fruit.

    # When people name something—"favorite fruit," for example—the name is usually connected to a particular type of thing.

    # The idea of "favorite fruit" only makes sense if it's connected to a kind of fruit. It just wouldn't make sense to connect it with a "monkey wrench" or "astronomy." 
    # Your brain does a good job of making sure names are matched up with the correct type of thing.

    # In a similar way, Python keeps track of the type of value associated with variables. 
    # While Python is dynamically typed and lets you change a variable's type, it still uses the type of the value to determine what operations are valid.
#

# How Python Handles Type Consistency

    # 1. Valid Operations: 
    # Python ensures you don't perform nonsensical operations, like trying to multiply a text string by an integer, which is usually not allowed:
#

# Valid operation: Multiplying an integer by an integer
price = 10
total = price * 3
print(total)
# Output: 30

# Invalid operation (Type Error): Python prevents this because it doesn't make sense
text = "hello"
# result = text * "world" 
# This would cause a TypeError because you can't multiply two strings.


# 2. Naming Convention: 
    # In Python, it's a best practice to keep variable names aligned with the type of data they hold (even if Python doesn't enforce it):
# 

# Good practice: The name matches the string type
user_name = "Alex"

# Less confusing than:
# user_name = 42

# Python's goal is to make sure your variables and values "make sense" together, preventing you from accidentally making a value a "banana" when your code logic expects a "shirt" (a string when you need a number, for example).