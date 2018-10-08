#Write your function here
def larger_sum(lst1, lst2):
  x = y = 0
  for i in range(len(lst1)):
    x += lst1[i]
  for i in range(len(lst2)):
    y += lst2[i]
  if x >= y: 
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
