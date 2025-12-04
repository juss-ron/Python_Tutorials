# Breaking It Down
#
# Each verse of the nursery rhyme follows a pattern:
#
# The first two lines are the same in each verse.
# The next two lines change in each verse.
# You take a breath between verses.
#
# When programmers are faced with a long list of tasks, like printing the original nursery rhyme, they often break the single long list down into multiple smaller lists. 
# This is called decomposition. 
# When you're choosing how to break apart your list, it's helpful to find the smallest pieces of work that are still meaningful. 
# For example, to split a single verse into multiple meaningful functions, you could do this:
#

def row_the_boat():
    print("Row, row, row your boat")
    print("Gently down the stream")

def merrily_dream():
    print("Merrily, merrily, merrily, merrily")
    print("Life is but a dream")

def breathe_between_verses():
    print("        ~        ")

#
# Now you can use these functions to print the first verse and the start of the second verse like this:
#

row_the_boat()
merrily_dream()
breathe_between_verses()
row_the_boat()

#
# Exercise
# Write a function called crocodileScream() for the second two lines of the second verse, and call it to complete the song in the console.
#



#
# Next, learn about making larger groups of tasks.