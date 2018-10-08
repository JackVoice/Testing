#Write your function here
def over_nine_thousand(lst):
  result = 0
  for i in range(len(lst)):
    if result < 9000: 
      result += lst[i]
    else:
      break
  return result

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
