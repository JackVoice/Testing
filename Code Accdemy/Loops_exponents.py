#Write your function here
def exponents(bases, powers):
  result = []
  for i in range(len(bases)):
    for j in range(len(powers)):
      result.append(bases[i] ** powers[j])   
  return result   

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
