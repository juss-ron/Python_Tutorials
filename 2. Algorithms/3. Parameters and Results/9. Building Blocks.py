# Building Blocks
    
    # When you were first introduced to functions it was as a way of grouping tasks together. Each function was a building block for a larger program.
    
    # Now you’ve learned that functions can also:
    
        # Take information in
        # Do work
        # Return information
 
    # Building blocks like this are much more powerful.
    
    # This function can be used to build a list:

def list_by_adding(item: str, to_list: str) -> str:
    return to_list + "\n" + item

list = "Milk"
list = list_by_adding(item="Eggs", to_list=list)
list = list_by_adding(item="Bread", to_list=list)

#
# Compare this to the way you were building lists before, with compound assignment:
#

list += "\n" + "Rice"

print(list)

#
# You’ll probably notice that your code is easier to read when you use this convenience function. 
# You no longer have to use "\n" to separate the items in the list. 
# Hiding complexity is one of the key benefits that functions bring to your code.