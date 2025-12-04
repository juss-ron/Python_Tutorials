# Defining a variable :
    # Start with the variable name or identifier e.g favourate_food
    # Place the asignment operator =
    # Place the value that the variable will hold
#

place_of_birth="Zimbabwe"
age=14

#
    # Once you've declared a variable, you can assign a new value to it:
#

place_of_birth="Zambia"

# Experiment
    # Below, add a line of code that assigns a new value to currentLocation:
#



# Part 2
    # Working with Variables

    # Now that you know how to declare variables, how and when do you use them?

        # You use variables in places where a value in your program needs to change over time. 
        # An example would be the score of a game. 
        # As the player scores more points, your code would update the value of a variable keeping track of the score.

    # For example this variable will be assigned an initial value of zero:
#

score = 0

#
    # If the player scores ten points, you can update the score:
#

score = 10

#
    # Now the player scores another five points, so you can update the score again:
#

score = 15

#
    # This is nice, but it would be nicer to use the existing value of score when calculating the new value.
    # To add another five points, you can do this:
#

score = score + 5

#
    # It might seem strangely circular to set a value to equal itself plus something else, as if you're both setting a value and changing it in a single step, but that isn't exactly what's happening.
    # Even though it’s a single line of code, it is evaluated the statement in two different steps.

    # The right side of the assignment is calculated first, as if it were written on its own. 
    # However, just doing a calculation with a variable doesn't change its value:
#

score + 5
score
score + 3

#
    # As you can see, after printing the value it remais as 20
#

print(score)

#
    # But when a calculation is on the right side of an assignment, the variable stores the calculation's result and takes on a brand new value:
#

score = score + 5
score = score + 3

#print(score)

# Experiment
    # What do you think the value of score would be after these lines? Try it and find out!

# Example
    # score = 5
    # score = score + score
#


 
# Shortcuts 
    # You saw how to use the current value of a variable as part of updating to a new value:

    # Value is initially zero
#

number = 0

#
    # Take the current value of `number`, add 2, assign the result to `number` as its new value
#

number = number + 2

#
    # This type of operation happens often enough that Swift has a special operator +=. 
    # This shorthand merges addition (+) and assignment (=) into one combined operation.

    # The following line of code:

    # score = score + 2
    # has the same effect as:
    # score += 2
#


