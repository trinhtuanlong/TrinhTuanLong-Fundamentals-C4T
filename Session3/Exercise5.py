def selection_sort(n):
  b = list(n[0])
  b.remove("[")
  n[0] = "".join(b)
  b = list(n[len(n)-1])
  b.remove("]")
  n[len(n)-1] = "".join(b)
  return print(sorted(n))
n = list(input("Your list:").split(","))
selection_sort(n)
    