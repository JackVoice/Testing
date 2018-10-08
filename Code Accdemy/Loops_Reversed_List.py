#Write your function here
def reversed_list(lst1, lst2):
  if len(lst1) == len(lst2):
    for i in range(len(lst1)):
      if lst1[i] != lst2[len(lst2) - 1 - i]:
        return False
        break
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
