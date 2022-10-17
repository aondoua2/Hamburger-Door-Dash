# Oliver Escobar, Karl Nordgren, Ashley Ondoua, Thayne Evans, Tayler Howard, Zack Olsen

import random

# ASK!!! The constructor should call the randomBurgers() method and assign the return 
# value to the burger_count instance variable
class Order:
    def __init__(self, randBurger):
        self.burger_count = 0
        self.randBurger = randBurger
        # randBurger = randBurger

    def randomBurgers(self):
        self.randBurg = random.randrange(1,21)

        return self.randBurg
        
class Person:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def customerName(self):
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]

class Customer(Person):
    def __init__(self, order):
        super().__init__()
        self.order = order



burgOrder = Order(10)
burgOrder.randBurger = burgOrder.randomBurgers()
print(burgOrder.randBurger)
