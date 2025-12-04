# Control Flow

    # Take a second to think about how functions affect the sequence of actions in your code. 
    # How can you figure out when each statement in your code will be executed? 
    # The order that code executes in a program is called control flow.

    # You're used to seeing the normal sequential flow of code, which follows the instructions in the order they appear. 
    # You've also experimented with creating functions, inside of which are more sequences of instructions. 
    # But when your code calls a function, the following line doesn't execute until after the function returns—that's not simple sequential execution.

    # Here's how to trace control flow through code that uses functions. 
    # Start by finding the first executable statement that's not in a function. 
    # (Remember that function declarations don't execute code; they just define it.) 
    # Sequential statements execute in the order they appear in the code segment. 
    # In the code below, the first statement that executes is on line 22, which assigns an empty string to the variable list.
#

def list_by_adding(item: str, to_list: str) -> str:
    new_list = to_list + "\n- " + item
    return new_list

list = ""
number_of_items = 0

list = list_by_adding(item="Milk", to_list=list)
number_of_items += 1
list = list_by_adding(item="Eggs", to_list=list)
number_of_items += 1
list = list_by_adding(item="Bread", to_list=list)
number_of_items += 1

print(f"Your shopping list contains {number_of_items} items:{list}")

#
    # The two assignments on lines 22 and 23 execute in order. 
    # The next executable code, on line 25, calls the list_by_adding function. 
    # When a function call happens, the normal sequential flow of your program is interrupted. 
    # Instead of continuing to line 26, control is transferred to the function, which means that the next line of code to execute is line 19. 
    # On line 20, the function returns a value. 
    # When a function executes a return statement or when the end of its code is reached, control passes back to the code that calls it. 
    # Recall that control flow was transferred to the function on line 25. 
    # That line now continues executing by assigning the value returned from listByAdding to list.

    # The flow moves on to line 26, and a similar pattern continues through the rest of the program.

    # Next, learn about how to choose names for your functions and parameters that will make it easier to understand the work they do.
#