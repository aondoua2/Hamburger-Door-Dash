# Tracking the Number of Hamburgers Eaten by Each Customer of Hamburger Door Dash
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
                
                

burgOrder = Order()
# burgOrder.randBurger = burgOrder.randomBurgers()
print(Person().customerName(), burgOrder.randBurger)

# iSearch = Person.customer_name 
# if iSearch in dictCustomer :


# object creation for the person class since it does not inherit from order class
personOrder = Person()

for iCount in range(0, burgOrder):
    print(Person().customerName(), burgOrder.randBurger)





    
numCustomer = int(input("How many customers do you want to enter: "))

queueCustomers = []
newCustomer = 100

for iCount in range(1, numCustomer + 1): #It is plus one because it is not inclusive right?
    iRandomName = Person().customerName()
    iRandomBurger = burgOrder.randBurg
    queueCustomers.append(iRandomName)
    if iRandomName in dictCustomer:
        dictCustomer[iRandomName] = dictCustomer[iRandomName] + burgOrder
        # Just printing out the outputs to see if it works.
        # print (iRandomName, " - ", dictCustomer[iRandomName])
        dictCustomer[iRandomName] + iRandomBurger
    queueCustomers.pop[0]
    #   dictCustomer[iSearch].customer_name = dictCustomer[iSearch].customer_name + randBurg

# if we want to print the customer list -- just playing with the code for now
for iCustomer in range (0, len(queueCustomers)):
    print(str(queueCustomers)) # i will fix this later!
   


iBurgerCount = "Jefe" + burgOrder.randBurger



# Compile the dictionary into a list that is sorted from high to low. Print each name with the corresponding burger value.
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True)
for customer in range(0, len(listSortedCustomers)):
    print(listSortedCustomers[customer][0].ljust(19), listSortedCustomers[customer][1])
# print(listSortedCustomers[customer - 1:customer], + '\n')
    #listSortedCustomers[0].ljust(19) I don't understand how ljust() works
    print(listSortedCustomers[0:1])
