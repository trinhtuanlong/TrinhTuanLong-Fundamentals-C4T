DNA = input("DNA:")
dict = {}
for k in range(len(DNA)):
  a = []
  for i in range(len(DNA)-k):
    b = []
    for j in range(i,i+k+1):
      b.append(DNA[j])
    a.append(str(b))
    dict[k+1] = a
print(dict)
    

    