#Write your function here
def append_size(lst):
  count = list(range(1, len(lst) + 1))
  lst += count
  return lst
#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
