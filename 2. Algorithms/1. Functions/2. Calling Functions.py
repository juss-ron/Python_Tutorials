# Calling a Function
#
# You’ve already taken advantage of abstraction and functions when you used print() to print “Hello, world!” to the console. 
# In Python, print() is a function. When you use it, you are calling the function:
#

print("Hello, world!")
print(360)

#
# Another example is the type() function. This funcion checks for the type of a value.
#

type(4)

#
# It can also check the type of a variable
#

name = "Jacob"
type(name)

# 
# You can use both functions by printing the type of a value
#

print(type(name))
print(type(44))

# Just as you perform many activities when you get dressed, many things happen when you call the print() function, including:
#
# Turning whatever you give it, including numbers, into a string.
# Adding a newline character, so each call to print() ends up on a new line.
# Making that string show up in the console.
#
# In this case, you’re calling a function that someone else has already created. 
# You don’t need to know every detail about how print() works in order to call it.
#
# Reusability is a large part of what makes functions so powerful. 
# They provide a way to combine detailed steps into a definition that can be used again and again.
#
# For the rest of this playground, you’ll practice calling functions and you'll learn how to define functions of your own.