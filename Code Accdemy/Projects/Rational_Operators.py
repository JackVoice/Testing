def greater_than(x,y):
  if x == y:
    return "These numbers are the same"
  if x>y:
    return x
  if x<y:
    return y

print(greater_than(2,4))
print(greater_than(7,4))
print(greater_than(-50,-50))

def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
  else:
    return "You don't have enough credits"

print(graduation_reqs(50))
print(graduation_reqs(120))
