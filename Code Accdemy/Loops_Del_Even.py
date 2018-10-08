#Write your function here
def delete_starting_evens(lst):
  for i in range(len(lst)):
    if i + 1 == len(lst):
      if lst[i] % 2 == 0:
        lst = []
    elif lst[i] % 2 != 0:
        lst = lst[i:]
        break      
  return lst
      

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
