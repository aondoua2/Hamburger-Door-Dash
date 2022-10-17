# Oliver Escobar
# Karl Nordgren

import random

class Order:
    def __init__(self, randBurger):
        self.burger_count = 0
        self.randBurger = 10

    def randomBurgers(self):
        randBurg = random.randrange(1,21)
        return randBurg
        
class Person:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def customerName(self):
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]

class Customer(Person):
    def __init__(self, order):
        super().__init__()
        self.order = order



order = Order(10)
order.randBurger = order.randomBurgers()
print(order.randBurger)
