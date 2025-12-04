# 🐍 Giving Values Back in Python
 #  
 # Over the last few exercises, you've developed functions that can use input values to build a sentence and then print the result to the console.
 #
 # Building the sentence and printing it are actually two separate jobs.
 # There could be cases when you want to build the sentence but not print it immediately. 
 # You might want to do further work on the sentence or display it in a user interface later.
 #
 # The best way to handle this is by having the function return the sentence as a value, rather than printing it inside the function.
 #
 
# Exercise
 # Write a function that takes the categoryOfThing and favorite as arguments, and returns a String. 
 # You should be able to call the function like this:
 #
 # let sentence = makeFavorite(categoryOfThing: "food", favorite: "cheese")
 
 #sentence should then have the value "My favorite food is cheese".
 
 #Remember that -> is used to say that a function returns a value.



# Experiment
 # Call your new function a few times with some different categories, assigning each result to a different constant. 
 # Why not try categories like food, movie, school subject or band?



# Exercise
 # Now that you have your results, you can use string interpolation to combine them into a self-introduction. Yours might look something like this:
 # "Hello, my name is Euna. \(favoriteFood) \(favoriteVideoStar) ..."


