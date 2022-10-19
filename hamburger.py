# Oliver Escobar, Karl Nordgren, Ashley Ondoua, Thayne Evans, Tayler Howard, Zack Olsen

import random

class Order:
    def __init__(self):
        self.burger_count = 0
        self.randBurger = 0

    def randomBurgers(self):
        self.randBurg = random.randrange(1,21)
        return self.randBurg
        
class Person:
    def __init__(self):
        self.customer_name = ""

    def customerName(self):
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        self.customer_name = random.choice(self.asCustomers)
        return self.customer_name
class Customer(Person):
    def __init__(self, order):
        super().__init__()
        self.order = order


burgOrder = Order()
# burgOrder.randBurger = burgOrder.randomBurgers()
print(Person().customerName(), burgOrder.randBurger)
