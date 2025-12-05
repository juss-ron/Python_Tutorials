# Equality

    # You’ve learned that true and false are special values. 
    # Without typing in Bools directly (which isn’t really making a decision), how do you ask questions in code? 
    # One way is by making comparison statements.

    # Comparison statements say something, and Python will say if that something is true or false. 
    # A comparison statement has three parts:
        # This…
        # has a relationship to…
        # that

    # Parts 1 and 3 are values, like the numbers and strings you’ve already been working with. Part 2 is something new: 
        # a comparison operator. Here’s an example:
#

# Print the statement below to see the result on the console
1 == 2

#
    # The double equal sign ==, or equality operator, checks if the left-hand and right-hand sides of the statement are equal. 
    # In this case, they’re not equal, so the statement is false.

    # Note
        # You can’t use a single equal sign = for a comparison because it’s already used for assigning a value, as you learned in previous playgrounds.

    # The following slightly more complicated example statement is true:
#

# Print the statement below to see the result on the console
10 == 9 + 1

#
    # It makes sense that the equality operator has lower precedence than arithmetical ones—you want to evaluate all expressions on either side before making the comparison.

    # Named values can also be used in comparisons:
#

hundred = 100
ten_times_ten = 10 * 10
nine_times_ten = 9 * 10

hundred == ten_times_ten
hundred == nine_times_ten


# Experiment
    # Try some comparisons of your own. Can you check if two string values are equal?

# Enter code below



# Find out more ways to compare values on the next page.