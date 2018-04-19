class Food():
  def __init__(self): None
class Customer():
  def __init__(self):
    self.name = input("What is your name?")
    self.order = list(input("Give me:").split(","))
class Employer():
  def __init__(self,order): None
  def response(self):
    print("Your lunch is being prepared.")
class Lunch():
  def __init__(self): None
  def f(self,order): return print("Your lunch is here.")
A = Customer()
B = Employer(A.order)
B.response()
C = Lunch()
C.f(A.order)


