"""
INTRODUCTION

In this exercise, we will simulate the classic economic model of supply and 
demand! It will require you to use all the tools you've learned at the start
 of the quarter, from lists to classes. In this scenario, each consumer has 
 only a single willingness to pay and buys at most a single item. Each producer
 has a single cost and sells at most a single item. The hints are extensive, 
 but you'll still need to think about how to implement this!
"""

"""
EXERCISE 1

Create templates that can mimic consumers and producers. The former should 
have a willingness to pay, and the latter should have a cost.

Hint: Create a class named Consumer with a single attribute: willingness_to_pay. 
Similarly, create a class named Producer with a single attribute: cost. Both of 
these attributes should be taken as arguments and assigned to the object upon 
initialization.
"""
class Consumer:
    def __init__(self, willingness_to_pay):
        self.willingness_to_pay = willingness_to_pay

class Producer:
    def __init__(self, cost):
        self.cost = cost


"""
EXERCISE 2

Create a set of 10 consumers using the market demand equation P = 10 - Q and 
10 producers using the market supply equation P = Q.

Hint: Start with the consumers. Determine the maximum and minimum demand 
values manually. Iterate over the range and calculate the corresponding 
"Price" using the equation. Create a consumer object using the price as 
willingness_to_pay and append it to a list of consumers to create an iterable 
list.

Repeat this process for the producers, but instead of willingness_to_pay, 
use the "price" as the cost.
"""
class Consumer:
    def __init__(self, willingness_to_pay):
        self.willingness_to_pay = willingness_to_pay

class Producer:
    def __init__(self, cost):
        self.cost = cost

# Create list of consumers based on the demand equation P = 10 - Q
consumers = [Consumer(willingness_to_pay=10 - q) for q in range(1, 11)]

# Create list of producers based on the supply equation P = Q
producers = [Producer(cost=q) for q in range(1, 11)]

# Display willingness to pay for consumers and costs for producers
consumers_wtp = [c.willingness_to_pay for c in consumers]
producers_costs = [p.cost for p in producers]

(consumers_wtp, producers_costs)
([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
"""
EXERCISE 3

Create a function to estimate the quantity demanded given a price and a list 
of consumer objects. Create another function to estimate the quantity supplied g
iven a price and a list of producer objects.

Hint: The quantity_demanded function should iterate over the set of consumers. 
If the consumer's willingness to pay exceeds the price, increase the q
uantity_demanded counter. Return this counter. The quantity_supplied 
function is similar.
"""
def quantity_demanded(price, consumers):
    """Calculate the quantity demanded at a given price."""
    count = 0
    for consumer in consumers:
        if consumer.willingness_to_pay >= price:
            count += 1
    return count

def quantity_supplied(price, producers):
    """Calculate the quantity supplied at a given price."""
    count = 0
    for producer in producers:
        if producer.cost <= price:
            count += 1
    return count

# Test the functions with a price example
test_price = 5
demanded = quantity_demanded(test_price, consumers)
supplied = quantity_supplied(test_price, producers)

(demanded, supplied)
(5, 5)

"""
EXERCISE 4

Find the equilibrium price and quantity.

Hint: Recall that the equilibrium price is the price at which quantity 
supplied equals quantity demanded.

Iterate over a set of prices. Find the quantity demanded and the quantity 
supplied at each price. If the two are equal, end the loop and print the 
corresponding price and quantity.
"""
def find_equilibrium_price_and_quantity(consumers, producers):
    """Finds the equilibrium price and quantity based on the consumer and producer lists."""
    for price in range(11):  # Assuming price ranges from 0 to 10 based on the previous equations
        demanded = quantity_demanded(price, consumers)
        supplied = quantity_supplied(price, producers)
        if demanded == supplied:
            return price, demanded  # Can return either demanded or supplied, they are equal at equilibrium

# Find and display the equilibrium price and quantity
equilibrium_price, equilibrium_quantity = find_equilibrium_price_and_quantity(consumers, producers)
(equilibrium_price, equilibrium_quantity)
 (5, 5)