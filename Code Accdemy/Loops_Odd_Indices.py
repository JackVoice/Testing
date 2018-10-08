#Write your function here
def odd_indices(lst):
  result = []
  for i in range(len(lst)):
    if i % 2 != 0:
      result.append(lst[i])
  return result
      

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
