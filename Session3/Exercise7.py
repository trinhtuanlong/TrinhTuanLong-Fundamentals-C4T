class rectangle():
  def __init__(self):
    self.w = float(input("Width:"))
    self.h = float(input("Height:"))
  def area(self):
    return self.w*self.h
a = rectangle()
print(a.area())