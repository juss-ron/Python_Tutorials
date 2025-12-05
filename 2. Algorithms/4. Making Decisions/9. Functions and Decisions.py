# Functions and Decisions

    # Conditionals are perfect opportunities to write helpful functions. 
    # If you have some decision-making code that doesn't read easily or makes things look too complicated, 
    # you can wrap it in a function and make it look like you’re asking a question.

    # Take your gig decision from the previous page. 
    # The final logic of the decision, used at the site of the if statement, 
    # means that you have to parse out the entire conditional every time you read through the code.

    # Instead, you can create a function that returns a Bool value to encapsulate all the necessary logic.
#

def bandCanCarryGear(band_member_count: int, gear_weight: int, bulkiest_item_weight: int, chance_of_rain: float) -> bool:
    maximum_trip_count = 2
    weight_per_person = 50
    total_carrying_capacity = band_member_count * weight_per_person * maximum_trip_count
    
    return gear_weight < total_carrying_capacity & (chance_of_rain < 0.1 | bulkiest_item_weight < 80)

#
    # This approach hides the complexity of the decision. 
    # Functions that return a Bool can be used directly in an if statement, like this:
#

if bandCanCarryGear(band_member_count=5, gear_weight=650, bulkiest_item_weight=60, chance_of_rain=0.05):
    "Rock on."
else:
    "Everyone quits! Looks like you've got a solo show."

#
    # Now anyone reading the code should be able to understand what it’s doing. 
    # (It looks like you need to hire another drummer, or leave some speakers behind.)

    # Continue your rock and roll adventure on the next page.