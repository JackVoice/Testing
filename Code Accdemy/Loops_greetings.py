#Write your function here
def add_greetings(names):
  result = []
  for i in range(len(names)):
    result.append("Hello, " + names[i])
  return result

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
