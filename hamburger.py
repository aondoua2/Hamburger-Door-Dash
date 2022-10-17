# Oliver Escobar, Karl Nordgren, Ashley Ondoua, Thayne Evans, Tayler Howard, Zack Olsen

import random

# ASK!!! The constructor should call the randomBurgers() method and assign the return 
# value to the burger_count instance variable
class Order:
    def __init__(self):
        self.burger_count = 0
<<<<<<< HEAD
        self.randBurger = 10
=======
        # randBurger = randBurger
>>>>>>> a5a931569e8ce057d73b5dc850b17ce6b38e163f

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
