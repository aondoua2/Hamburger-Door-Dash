# Oliver Escobar
# Practice for Burger Assignment

import random


class Order: 
    def __init__ (self, randomBurger):
        self.randomBurger = randomBurger
        self.burgerCount = 0

    def randomBurger(self):
        return random.randrange(1,21)

class Person:
    def __init__(self):
        self.customerName = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        self.currentName = ""

    def randomName(self):
        self.currentName = random.choice(self.customerName)
        return (self.currentName)

myCustomer = Person().randomName()
print (myCustomer)
