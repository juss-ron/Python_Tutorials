# Compound Conditionals

    # Imagine your five-person band gets a gig, and you have 450 pounds of equipment to haul from your van to the stage. 
    # You know that each member of the band can carry 50 pounds of gear per trip, but if anyone has to make more than two trips, they swear they’ll quit on the spot. 
    # So you do some arithmetic to figure out whether or not the band should accept the gig:
#

band_member_count = 5
weight_per_person = 50
maximum_trip_count = 2

gear_weight = 450

total_carrying_capacity = band_member_count * weight_per_person * maximum_trip_count

if gear_weight < total_carrying_capacity:
    "Rock on."
else:
    "Everyone quits! Looks like you've got a solo show."

#
    # Then you take the gig, and your band quits anyway! 
    # One of the pieces of equipment weighed 100 pounds and it was raining when you arrived—nobody wanted to get wet hauling the heavy gear. 
    # So it looks like your decision is more nuanced: If rain seems probable, you shouldn't have any gear that's difficult to carry. 
    # In summary, you should only take a gig if:

        # You can handle all the gear in two or fewer trips, 
        # and either it's unlikely to rain or you don't have any especially bulky gear.

    # That's doable using some if...else magic, like this:
#

chance_of_rain = 0.5
bulkiest_item_weight = 60

if gear_weight < bulkiest_item_weight:
    if bulkiest_item_weight < 80:
        "Rock on."
    elif chance_of_rain >= 0.1:
        "Everyone quits! Looks like you've got a solo show."
else:
    "Everyone quits! Looks like you've got a solo show."

#
    # But that code is less than elegant. 
    # One result is duplicated due to the complex logic expressed by multiple if and else statements. 
    # In addition, the nested code isn't very clear to read—any manager that came after you would have a hard time tweaking your algorithm. 
    # And of course, adding new factors would produce even more tangled code.

    # The solution lies with Boolean operators. 
    # The key terms from your complex decision are the words "and" and "or"—which correspond directly to operators that combine two Bool values and evaluate to a Bool result.

    # The Boolean AND operator is written &. It produces true only when both its operands are true:
#

False & False
True & False
False & True
True & True

# The Boolean OR operator is written ||. It produces true if either (or both) of its operands are true:

False | False
True | False
False | True
True | True

#
    # You can combine simple conditionals with these operators, as well as the Boolean NOT operator, ! and parentheses, to form new compound conditionals. 
    # Equipped with these new tools, you could write a different version of the code. Compare the code below to the one above. 
    # Will they have the same or a different result?
#

if gear_weight < total_carrying_capacity & (chance_of_rain < 0.1 | bulkiest_item_weight < 80):
    "Rock on."
else:
    "Everyone quits! Looks like you've got a solo show."

#
    # This code has the same effect as the one above, although this code is much cleaner. 
    # But you can still do better. Next, learn about using functions as conditionals to completely encapsulate complex decisions.
#

