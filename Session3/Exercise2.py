attempts = 0
while True:
  attempts += 1
  response = input("Do you want to quit?(y/n)")
  if response != "y" and response != "n": print("Only accept y or n.")
  elif response == "n": continue
  else: break
print("Exiting after",attempts,"attempts")
    