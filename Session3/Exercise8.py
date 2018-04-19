class Car():
  def __init__(self):
    None
  def setBrand(self):
    self.Brand = input("Brand:")
  def setMaxSpeed(self):
    self.MaxSpeed = input("Max Speed:")
  def printData(self):
    if self.Brand[0].lower() in "aeiou": n = "an"
    else: n = "a"
    print(n,"%s with max speed %s"%(self.Brand,self.MaxSpeed))
a = Car()
a.setBrand()
a.setMaxSpeed()
a.printData()