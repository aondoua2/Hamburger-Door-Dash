# Oliver Escobar
# Practice for Burger Assignment

import random


class Order: 
    def __init__ (self):
        self.burgerCount = 0

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
    def __init__(self, order):
        self.order = order

myCustomer = Person().randomName()
myQueueVariable = 100
Customer(myQueueVariable)
myDictionaryVariable = 0

print (myCustomer, Order().randomBurger())
