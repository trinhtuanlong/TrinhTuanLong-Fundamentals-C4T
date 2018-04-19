class string():
  def __init__(self):
    None
  def get_string(self):
    n = input("String:")
    return n
  def print_string(self,n):
    print(str(n).upper())
string = string()
string.print_string(string.get_string())