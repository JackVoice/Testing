def contains(big_string,little_string):
  if little_string in big_string:
    return True
  else:
    return False

def common_letters(string_one,string_two):
  storage = []
  for i in string_one:
    for j in string_two:
      if i == j:
        if i not in storage:
          storage.append(i)
  return storage
        
print(common_letters("banana", "cream"))
