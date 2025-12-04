# Naming

    # The function you defined early on in this playground was called like this:
        # hello(name: "Maya")

    # But there are two problems with this function:

    # The function has a side effect (the name is printed to the console) but this isn’t clear from the name. 
    # A function that has a side effect should have a verb in the name.
    # Functions should read as much like a sentence as possible. 
        # “Hello name Maya” is not a sentence.

    # To address the first problem, the function could be renamed. 
        # A better name would be print_hello.
         
    # But the function-as-a-sentence would still read “Print hello name Maya,” which still doesn't work. 
    # “Print hello to Maya” would be better:
#

def print_hello(to: str):
    print("Hello " + to)

print_hello(to="Maya")

# It is also possible to completely ignore the parameter name when calling the function

#
    # This function passes the side effect test and the function-as-a-sentence test.

    # Experiment
        # Think of some more tasks a program might perform. 
        # Write them out as sentences, then think about how those sentences would look as functions.

        # For example: “Get the first letter of 'Python' would be getTheFirstLetter(of: "Swift")

#