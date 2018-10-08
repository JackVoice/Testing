def get_boundaries(target,margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit
low, high = get_boundaries(100,20)
print("Low limit: " + str(low) + ", high limit: " +str(high))
