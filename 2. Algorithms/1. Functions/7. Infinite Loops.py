# Infinite Loops
#
# Programmers sometimes make the mistake of calling a function from itself. 
# When the function is called, it calls itself, which calls itself, which calls itself...
#
# A classic example from real life is found on shampoo bottles: “Lather, rinse and repeat.” 
# If those instructions were code, a computer would interpret them by lathering, rinsing, lathering and rinsing again, and so on. 
# You’d never leave the shower!
#
# This is called an infinite loop. 
# It's not really infinite, because in most cases it will cause the program to run out of memory and eventually crash (or the bottle will run out of shampoo).
#

def row_the_boat():
    print("Row, row, row your boat")
    print("Gently down the stream")

def merrily_dream():
    print("Merrily, merrily, merrily, merrily")
    print("Life is but a dream")

def verse_one():
    row_the_boat()
    merrily_dream()

verse_one()

#
# Experiment
# Make an infinite loop in the code above by editing the row_the_boat function, so it calls row_the_boat() after printing. 
# Look at the console and the results sidebar. 
# Remove the line to stop the loop. It might take a while until the playground recovers – infinite loops are hard work. 

# Next, understand how functions make working on longer programs easier to understand.