#Write your function here
def divisible_by_ten(nums):
  Ans = []
  for i in range(len(nums)):
    if nums[i] % 10 == 0:
      Ans.append(nums[i])
  return len(Ans)

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
