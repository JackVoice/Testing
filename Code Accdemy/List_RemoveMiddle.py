#Write your function here
def remove_middle(lst,start,end):
  first_half = lst[0:start]
  second_half = lst[end + 1:]
  return first_half + second_half

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
