def letter_check(word,letter):
  counter = 0
  for i in word:
    if i == letter:
      counter += 1
  if counter >= 1:
    return True
  else:
    return False
    
   
