# Hamburger Door Dash
# Oliver Escobar, Karl Nordgren, Ashley Ondoua, Thayne Evans, Tayler Howard, Zack Olsen

import random

# Imported from original code (Hamburger.py)
class Order:
    def __init__(self):
        self.burgerCount = self.randomBurger()

    def randomBurger(self):
        self.burgerCount = random.randrange(1, 21)
        return self.burgerCount


class Person:  # CHANGE PERSON CLASS TO INIT TO RANDOM
    def __init__(self):
        self.customerName = self.randomName()

    def randomName(self):
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        customerName = random.choice(self.asCustomers)
        return customerName


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

# This is a dictionary data type. It holds the values for the customers' names and the number of orders.
queueCustomers = []
dictCustomer = {}
newCustomer = 100
firstCustomer = Customer()

# This is the code for the Queue.
for iCount in range(1, newCustomer + 1):  # It is plus one because it is not inclusive right?
    iRandomName = Customer()
    queueCustomers.append(iRandomName)
    # This is the code that adds Dictionary inputs.

while len(queueCustomers) > 0:
    if queueCustomers[0].customerName in dictCustomer:
        dictCustomer[queueCustomers[0].customerName] += queueCustomers[0].order.burgerCount
    else:
        dictCustomer[queueCustomers[0].customerName] = queueCustomers[0].order.burgerCount
    queueCustomers.pop(0)

    # Print out each customer and their total burgers ordered sorted by the most number of burgers ordered
print("\n", "".ljust(5), "Top Customers")
print("-" * 27)
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True)
# This for loop prints the value in the the sorted customer list.
for customer in range(0, len(listSortedCustomers)):
    print("|", str(listSortedCustomers[customer][0]).ljust(19), str(listSortedCustomers[customer][1]).ljust(3), "|")
print("-" * 27, "\n")