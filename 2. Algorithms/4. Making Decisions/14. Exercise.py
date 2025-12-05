# Similar, Yet Different

    # On the Conditionals page, you learned that code that looks correct can produce the wrong result. If/else statements are tricky to get right when you're first learning about them. There are two rules to keep in mind:

        # Multiple if statements appearing sequentially will all get executed.
        # In an if/else statement with multiple "else if" or "else" clauses, only one will execute—the first one that evaluates to true.

    # This page has some code samples with errors. You'll observe how they work and then fix them.

    # The code segment below converts number grades to letter grades according to the following rules:

        # F's are below 70.
        # C's are between 70 and 79.
        # B's are between 80 and 89.
        # A's are 90 or greater.
#

grade = 47

if grade < 70:
    print("You got an F 😭")

if grade >= 70:
    print("You got a C 😕")

if grade >= 80:
    print("You got a B 😌")

if grade >= 90 :
    print("You got an A 🤩")

#
    # Try to predict what happens as you increase the score. What will the program print?

    # Exercise
        # Fix the code so that it prints the correct outcome. You might do that by reordering it, or by using else clauses.

    # Now look at the next code segment. 
    # It was written by your (somewhat demanding) bandmate, who explained how they came up with the logic:

    # If a gig is more than 20 miles away, our manager needs to bring something for me to read. 
    # If it's less than five miles away, tell them I'll leave extra early to exercise and get some steps in. 
    # But if it's more than 100 miles away, I'm not really interested in playing—they should find a sub for me. 
    # Otherwise I'm super low maintenance.
#

gig_distance = 6

if gig_distance > 20:
    print("I need something to read.")
elif gig_distance < 5:
    print("I'll meet you there.")
elif gig_distance > 100:
    print("Better find somebody else on bass.")
else:
    print("You know me—I'm easy! Let's hop in the van.")

# Exercise
    # Try testing the code with different distances. 
    # Then fix the code (and tell your bandmate they should take a Swift programming course).
