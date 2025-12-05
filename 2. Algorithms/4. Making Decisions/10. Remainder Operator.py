# Remainder Operator

    # Your band hired that extra member and has gone on tour. But there’s more trouble.

    # They insist on a bowl of candy in the dressing room every night. 
    # If it doesn’t divide exactly between all of them, they’ll quit.

    # Remember from your first playground that you can use the remainder operator to find out if one number divides evenly into another. 
    # Can the candy be split evenly among your band members? Check if the remainder is zero:
#

band_member_count = 6
candy_count = 79
if candy_count % band_member_count == 0:
    print("Rock on.")
else:
    print("Everyone quits! This is unacceptable!")

#
    # When reading the code, it’s not completely clear what’s happening. 
    # The % and == 0 distract from the question that the code is asking. 
    # To make it clearer, you could put the code inside a function:
#

def isCandyAmountAcceptable(bandMemberCount: int, candyCount: int) -> bool:
    return candyCount % bandMemberCount == 0

#
    # As in the previous example, this approach hides the complexity of what’s happening in the function. 
    # You can then write the following code:
#

if isCandyAmountAcceptable(bandMemberCount=band_member_count, candyCount=candy_count):
    print("Rock on.")
else:
    print("Everyone quits! This is unacceptable!")

# Note
    # In some other programming languages % is called the modulo operator and has different behavior for negative numbers.

# Now summarize what you’ve learned.