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

queueCustomers = [Customer()]
for currentCustomer in Customer():
    currentCustomer = Person().randomName()
    queueCustomers.append = currentCustomer
    
# queueCustomers.append("El Guapo")
# queueCustomers.append("Lucky Day") 
# queueCustomers.append("Ned Nederlander")
# queueCustomers.append("Dusty Bottoms")
# queueCustomers.append("Harry Flugleman")
# queueCustomers.append("Carmen")
# queueCustomers.append("Invisible Swordsman")
# queueCustomers.append("Singing Bush")

print (myCustomer, Order().randomBurger())

iCustomers = int(input("How many customers do you want to enter: "))

for iCount in range(0, iCustomers) :
                iOrder = int(input("What is  "))
                customerName = input("What is the customers name: ")
                iRandBurger = int(input("How many burgers does this customer want? "))
                # dictCustomer[iOrder] = Person(customerName, iRandBurger)


# for customer in newCustomer:
    

iSearch = int(input("Which student would you like to update? "))
            
# if iSearch in dictCustomer :
#     iNew_Credits = int(input("How many credits should be added to the student? "))
#     dictCustomer[iSearch].total_credits = dictCustomer[iSearch].total_credits + iNew_Credits
#     print(dictCustomer[iSearch].first_name + " has " + str(dictCustomer[iSearch].total_credits))
# else :
#     print("Key not found")  


queueCustomers = [Customer()]
queueCustomers.append("Jefe") 
queueCustomers.append("El Guapo")
queueCustomers.append("Lucky Day") 
queueCustomers.append("Ned Nederlander")
queueCustomers.append("Dusty Bottoms")
queueCustomers.append("Harry Flugleman")
queueCustomers.append("Carmen")
queueCustomers.append("Invisible Swordsman")
queueCustomers.append("Singing Bush")