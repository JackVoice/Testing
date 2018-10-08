#Write your function here
def combine_sort(lst1, lst2):
  lst_comb = lst1 + lst2
  lst_comb.sort()
  return lst_comb
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
