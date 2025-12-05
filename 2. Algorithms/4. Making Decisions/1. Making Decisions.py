# Making Decisions

    # A code segment refers to a collection of program statements that are part of a program. 
    # All of the code segments you've written so far have run from the first line to the last, in order. 
    # No matter what you give your code to work on, it does the same things with it.

    # Consider the string interpolations you learned about. You had to perform a calculation and show the result in a string, something like this:
        # Making Decisions

    # A code segment refers to a collection of program statements that are part of a program. 
    # All of the code segments you've written so far have run in playgrounds — and run from the first line to the last, in order. 
    # No matter what you give your code to work on, it does the same things with it.

    # Consider the string interpolations you learned about. You had to perform a calculation and show the result in a string, something like this:
#

video_length = 3
videoLength_too_short_reaction = "If I blinked, I'd miss it!"
video_reasonable_length_reaction = "That was lovely."
video_message = f"Your video is {video_length} seconds long. {videoLength_too_short_reaction}"

#
    # If the answer was 3, then this works fine:

        # Your video is 3 seconds long. If I blinked, I'd miss it!

    # But try changing the video length to something enormous, like 2857013857. In that case, the videoMessage doesn’t look right:

        # Your video is 2857013857 seconds long. If I blinked, I'd miss it!

    # You want your code to do different things depending on the value of the answer. You need your code to make decisions.

    # Find out about the type used in Swift for making decisions.