# Change Something Once
# 
# Containing work in a function can make your life easier when things change. 
# You only need to change the code in one place, and you’ll know where to do it because you understand how the function works and what it does.
# 
# On this page, the functions merrilyDream(), crocodileScream(), repetitiveTheme() and breatheBetweenVerses() have already been defined.
#

def merrily_dream():
    print("Merrily, merrily, merrily, merrily")
    print("Life is but a dream")

def crocodile_scream():
    print("If you see a crocodile")
    print("Don't forget to scream")

def repetitive_Theme() :
    print("This song is quite repetitive")
    print("Can you spot the theme")

def breathe_between_verses():
    print("        ~        ")

#
# The other functions are declared below:
#

def row_the_boat():
    print("Row, row, row your boat")
    print("Gently down the stream")

def verse_one():
    row_the_boat()
    merrily_dream()

def verse_two():
    row_the_boat()
    crocodile_scream()

def verse_three():
    row_the_boat()
    repetitive_Theme()

verse_one()
breathe_between_verses()
verse_two()
breathe_between_verses()
verse_three()

#
# It's been decided that the rhyme shouldn't be about boats any more.
# Update the print statements in row_the_boat() so the song follows the same pattern but is about something else.
# The pattern is:
# verb, verb, verb “your” noun
# la la la la rhyme
#
# For example, you could use “Ride, ride, ride your bike”, “With your cycling team”
# 
# You only have to update two lines of code, but the changes will be in effect everywhere that function is called.

# Next, review what you’ve learned.