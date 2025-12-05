# 🐍 Getting Values Back (Returning Values) in Python

    # In Python, just like in Swift, functions can process input and then send a result back to the code that called them. 

    # To declare a Python function that returns a value, you need two main components:

        # Type Hint (Optional): 
            # You can add a return type hint using the arrow syntax (->) after the parameter list to indicate the type of value the function is expected to return (e.g., -> str).

        # return statement: 
            # The function body must include a return statement that specifies the value to be handed back.
#

def space_available_message(each_video_duration: int, numberOfVideos: int) -> str:
    # Set constant values
    current_space = 10000
    megabytes_per_video_second = 3
    
    # Calculate space used and space remaining
    space_used = each_video_duration * numberOfVideos * megabytes_per_video_second
    space_available = current_space - space_used

    # Return the result as a formatted string (str)
    return f"If your {numberOfVideos} videos are {each_video_duration} seconds each, you'll have {space_available} MBs remaining"

# Calling the function and seeing the returned value
print(space_available_message(each_video_duration=10, numberOfVideos=50))
# Output: If your 50 videos are 10 seconds each, you'll have 8500 MBs remaining

# 💡 Using the Returned Value
    # The value that a function returns is just like any other value (a string, an integer, etc.). It can be:

        # 1. Assigned to a variable: The most common use.
        # 2. Used as an argument for another function call.
        # 3. Used in an expression for further calculation or manipulation
#

# Variables can be used as the arguments passed into the function
desired_video_duration = 40
holiday_video_count = 100

# The function call is evaluated, and the resulting string is assigned to a variable
video_message = space_available_message(each_video_duration=desired_video_duration, numberOfVideos=holiday_video_count)
print(f"Video Message: {video_message}")

# The returned value (video_message) can be used to build other strings
named_video_message = f"Hey Micah! {video_message}"
print(named_video_message)

# Output:
# Video Message: If your 100 videos are 40 seconds each, you'll have -2000 MBs remaining
# Hey Micah! If your 100 videos are 40 seconds each, you'll have -2000 MBs remaining

# Functions as Expressions
# A function call that returns a value (like space_available_message(...)) is an expression because it is evaluated and produces a value. 
# Anywhere you can use a value, you can use a function call.
#
# Note: 
# A Python function can have multiple parameters, and although the standard practice is to return a single value, 
# it can easily return multiple values by packaging them into a single tuple (which is still considered one value/object).
#
# Would you like to try an exercise where you create a function that returns a value?