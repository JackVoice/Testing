#Write your function here
def append_sum(lst):
  count = 0 
  while count <= 2:
  	value = lst[-1] + lst[-2]
  	lst.append(value)
  	count += 1
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
