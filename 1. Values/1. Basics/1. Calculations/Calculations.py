# Calculations

    # You can use Python interactively, like a calculator.
    # Type in the math problem you want solved, and the console will show the answer, 
    # or the result, of the calculation when the code is run.

    # You can use the plus (+) and minus (-) signs for addition and subtraction, 
    # just as you'd expect:
#

print(34 + 56 + 230)
# Expected result: 320

print(1000 - 300)
# Expected result: 700

#
    # These signs are formally known as arithmetic operators.
    # The + operator performs an addition operation on the two values to either side. 
    # The asterisk (*) is the multiplication operator:

print(3 * 100)
# Expected result: 300

#
    # The division operator is the slash (/). 
    # IMPORTANT NOTE: Unlike some languages, Python's single slash (/) always performs 
    # FLOAT (decimal) division, even if the result is a whole number.
    # To perform INTEGER (floor) division (where the remainder is discarded), 
    # use the double slash (//).

# Example 1: Float division (returns a float)
print(24 / 8)
# Expected result: 3.0

# Example 2: Integer (Floor) division (discards the remainder)
print(17 // 3)
# Expected result: 5 (17 divided by 3 is 5 with a remainder of 2)

#
    # Note that Python observes the standard precedence of operations: 
    # Multiplication (*), Division (/ and //), and Modulo (%) before Addition (+) and Subtraction (-).
#

print(2 * 5 + 8)
# Expected result: 18 (2 * 5 = 10, then 10 + 8 = 18)

print(8 + 2 * 5)
# Expected result: 18 (2 * 5 = 10, then 8 + 10 = 18)

# And it performs same-precedence operations in order from left to right:

print(120 / 6 * 2)
# Expected result: 40.0 (120 / 6 = 20.0, then 20.0 * 2 = 40.0)

#
    # There's also a special % operator to calculate the remainder of a division. 
    # (You'll learn more about practical uses of the remainder, or modulo, operator later in this course.)
#

print(12 % 5)
# Expected result: 2 (12 divided by 5 is 2 with a remainder of 2)

# The remainder operator observes the same precedence as multiplication and division.

print(12 % 5 + 4 // 2)
# Breakdown: (12 % 5 = 2) + (4 // 2 = 2) = 4
# Expected result: 4

# For grouping, use parentheses ( ), which take precedence over all other operators:

print((8 + 2) * 5)
# Expected result: 50

print(120 / (6 * 2))
# Expected result: 10.0

print((300 + 500 + 400) / (6 / 2))
# Breakdown: (1200) / (3.0) = 400.0
# Expected result: 400.0

# Exercise

    # Practice using the code environment like a calculator. 
    # Edit some of the existing expressions above and add a few of your own. 
    # Notice that every time you make a change and run the code, the results are updated in the console.
#