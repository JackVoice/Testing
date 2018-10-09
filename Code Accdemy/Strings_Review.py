def username_generator(first,last):
  counter = 0
  username = ""
  for i in first:
    if counter <= 2:
      counter += 1
      username += i
  counter = 0
  for j in last:
    if counter <= 3:
      counter += 1
      username += j
  return username

def password_generator(username="testin"):
  password = ""
  counter = 0
  for i in username:
    password += username[counter -1]
    counter += 1 
  return password

print(password_generator())
