import random
# Imported from original code (Hamburger.py)
class Order: 
    def __init__ (self):
        self.burgerCount = self.randomBurger

    def randomBurger(self):
        self.burgerCount = random.randrange(1,21)
        return self.burgerCount

class Person:
    def __init__(self):
        self.customerName = ""

    def randomName(self):
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        self.customerName = random.choice(self.asCustomers)
        return (self.customerName)

class Customer(Person):
    def __init__(self):
        self.order = Order()

dictCustomer = {
                "Jefe" : 0,
                "El Guapo" : 0,
                "Lucky Day" : 0,
                "Ned Nederlander" : 0,
                "Dusty Bottoms" : 0,
                "Harry Flugleman" : 0,
                "Carmen" : 0,
                "Invisible Swordsman": 0,
                "Singing Bush": 0
                }


queueCustomers = []
newCustomer = 100

# This is the code for the Queue.
for iCount in range(1, newCustomer + 1): #It is plus one because it is not inclusive right?
    iRandomName = Person().randomName()
    queueCustomers.append(iRandomName)
    burgOrder = Order().randomBurger()
    # This is the code that adds Dictionary inputs.
    if iRandomName in dictCustomer:
        dictCustomer[iRandomName] = dictCustomer[iRandomName] + burgOrder
        # Just printing out the outputs to see if it works.
        print (iRandomName, " - ", dictCustomer[iRandomName])

# Print out each customer and their total burgers ordered sorted by the most number of burgers ordered

# This code does not work.
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True)
for customer in range(0, len(listSortedCustomers)):
    print(listSortedCustomers[0:1])
