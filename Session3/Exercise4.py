a = []
c = []
while True:
  b = tuple(input("Add tuple to your list:").split(","))
  if b == ("done",): break
  else:
    a.append(b)
for i in a:
  y = list(i)
  for j in range(len(i)):
    if j == len(i)-1:
      y[j] = 100
  c.append(tuple(y))
print(c)
  

    