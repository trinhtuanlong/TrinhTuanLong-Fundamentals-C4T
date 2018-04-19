def registration():
  users = {}
  while True:
    username = input("Registering Username:")
    if username == " ": break
    else: users[username] = input("Registering Password:")
  return users
def accept_login(users,username,password):
  m = 0
  for i in users.keys():
    if username == i:
      if password == users[i]:
        print("Login successful!")
        return True
        break
      else:
        print("Password incorrect!")
        return False
      break
    else: m += 1
  if m>0:
    print("Username not registered!")
    return False
users = registration()
while True:
  username = input("Username:")
  password = input("Password:")
  if accept_login(users,username,password): break
  
    