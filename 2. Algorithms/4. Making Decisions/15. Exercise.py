# Exercise: Leap Years

    # To decide if a year is a leap year, there are several decisions that have to be made in the correct order.

        # Is the year divisible by 4?

            # If so, is the year divisible by 100?
                # If so, is the year divisible by 400?
                    # If so, it is a leap year.
                    # If not, it is not a leap year.

                # If it's not divisible by 100, it is a leap year.

            # If it's not divisible by 4, it is not a leap year.

    # These decisions can be made inside a function as a series of nested if...else statements.

    # The number(number:, isDivisibleBy:) function has been built to make this exercise easier. 
    # Below is an incomplete function for deciding if a given year is a leap year:
#

def number(number: int, isDivisibleBy: int) -> bool:
    return number % isDivisibleBy == 0

def isLeapYear(year: int) -> bool:
    # Is the year divisible by 4?
    if number(year, isDivisibleBy=4):
        return True
    else:
        return False

# Should be true
print(isLeapYear(2000))
# Should be false
print(isLeapYear(1900))
# Should be true
print(isLeapYear(2012))
# Should be false
print(isLeapYear(2017))

# Exercise
    # Complete the function above so that the rules are all followed and the examples get the correct answers. 
    # Hint: Try using the rules as pseudocode by making them into comments. 
    # Then write the code that goes with each comment underneath it.

# Exercise
    # For a challenge, complete the function below. It should behave identically without using any nested conditional statements. 
    # Use a single level of if/else statements along with conditionals that use Boolean operators. 

    # Hint: Create constants that represent the three key conditions, and then compose a Boolean expression with those constants.

def isLeapYear2(year: int) -> bool:
