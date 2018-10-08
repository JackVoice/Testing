#Write your function here
def max_num(nums): 
  result = nums[0]
  for i in range(len(nums)):
    if nums[i] > result:
      result = nums[i]
  return result

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
