class Employee:
    order = []

    def takeOrder(self, foodName):
        print("Anything else?")
        self.order.append(foodName)  # return a Food, with requested name


class Customer:
    def __init__(self):
        self.food = []  # initialize my food to None

    def placeOrder(self, foodName, employee):
        self.food.append(foodName)  # place order with an Employee
        return self.food
    def printFood(self):
        print(self.food)  # print the name of my food


class Food:
    def __init__(self, name): None  # store food name


class Lunch:
    def __init__(self):
        self.cus = Customer()
        self.emp = Employee()  # make/embed Customer and Employee

    def order(self):
        while True:
            a = input("I want to order")
            if a == " Nothing else": break  # start a Customer order simulation
            else: self.emp.takeOrder(self.cus.placeOrder(a,self.emp))
        return self.emp.order

    def result(self):
        print("Your meal consists of:", self.emp.order)  # ask the Customer what kind of Food it has


a = Lunch()
a.order()
a.result()
