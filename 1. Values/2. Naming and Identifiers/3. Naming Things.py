# Naming Things

# In programming, names can be very descriptive and useful, helping you keep track of what’s what — just like the names you give things in real life. 
# In code, when you give a value a name, you can use that name everywhere you would use the value. 
# This is a form of abstraction that makes the code easier to read and understand.
#
# Names also help you avoid errors in your code. For example, it was easy to make a mistake in the pet show experiment, since you had to change a number in multiple lines of code for each update. But if you’d defined a name for each value (for example, the number of turtles), you would only need to change the definition of the name once and the updated definition would be used everywhere the name appears in your code.
#
# In Python, you can choose a name and associate it with a value by defining a variable. 
# You’ll explore variables in more detail later in the course. 
# For now, it’s enough to know that variables are a fundamental way of naming values in Python.
#
# Write a name to define a variable, and use the equal sign = to give a value to the variable:

number_of_dogs = 6

number_of_cats = 5

number_of_turtles = 2

number_of_hamsters = 1

#
# After you’ve defined a constant and assigned a value to it, you can use the constant wherever you would have used the value, including in mathematical calculations that define the value of yet another constant:
#

total_number_of_animals = number_of_dogs + number_of_cats + number_of_turtles + number_of_hamsters

total_number_of_mammals = number_of_dogs + number_of_cats + number_of_hamsters

print(f'There are {total_number_of_animals} animals')

print(f'There are {total_number_of_mammals} mammals')


#
# Now it will be much easier — and less error-prone — to update the number of a certain kind of animal. 
# You only have to update the value where the constant is defined.
#
# You can even let python do the math for you by adding or subtracting on the right-hand side of the equal sign. 
# For example, if two more people were bringing a dog, instead of changing the 6 to an 8, you could type:
#
# let numberOfDogs = 6 + 2


# Experiment
# 
# As the week goes on, you get even more information about people’s pets.
# Update the code above for the following updates:
#
# Two more people are bringing a dog.
# One of the cats cannot make it.
# The sick turtle is feeling much better and will be coming to the pet show.
# Another person is bringing a hamster.
#
# Once you’re finished experimenting, move ahead.