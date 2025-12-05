# Else

    # The code to display a video message contains two very similar statements. 
    # This approach can be slow, confusing, and, an easy way to make mistakes — as you saw in the experiment on the previous page.
#

video_length = 5

print("Two If statements")
if video_length >= 5:
    print("That's lovely.")

if video_length < 5:
    print("If I blinked, I'd miss it.")

#
    # What you really want is to be able to say “If the value is less than 5, do this; otherwise, do something else”. 
    # You can do that with the else keyword:
#

print("If else statement")
if video_length < 5:
    print("If I blinked, I'd miss it.")
else:
    print("That's lovely.")

# This is called an if/else statement. It works like this:

    # if…
    # some code that could be true or false is true…
    # run the code inside the braces: { ... }
    # else…
    # run the code inside the second set of braces

# Experiment
    # Change the value of video_length again. 
    # Confirm that the same results are shown from the multiple if statements and the if / else statement.

# Experiment
    # Change the values that video_length is compared to by changing all the 5 values to other values. 
    # Try to make both messages from the top if statements appear at the same time.

# No matter what you set the value of video_length to or what value you compare it to,
# only one message from the if/else statement will be displayed.

# Next find out how to include more than one conditional in your decision-making.
