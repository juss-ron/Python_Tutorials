# Exercise 2
#
# Your friend’s entrepreneurial spirit knows no bounds. Now your friend is running the town lottery.
#
# By naming things and only setting a value once, it's easier to figure out the correct way of calculating something. 
# Later, you can change the values and check the answers.
#

# Values you should edit
tickets_sold = 1000
ticket_price = 1
printing_costs = 20
advertising = 50

#
# Exercise
#
# You’ve done enough work for free for your friend. 
# In return for your help on this venture, your friend will give you a tenth of the profits. 
# The jackpot is half of the total ticket sales money. 
# Try changing the numbers above - tickets sold, ticket price, printing costs, or advertising costs  - and see if you can get your cut up to 100 or more.
#
#The calculations below are fixed, but you can change the results by changing the numbers above:
#

# Total takings
total_takings = ticket_price * tickets_sold

# Jackpot
jackpot = total_takings / 2

# Expenses
total_expenses = printing_costs + advertising

# Profit
profit = total_takings - jackpot - total_expenses

# Distribution
programmers_cut = profit / 10 # This is the answer you want to get > 100! 👉 
friends_cut = profit - programmers_cut

print(f'The programmer gets {programmers_cut}')
