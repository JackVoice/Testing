import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random
# Add your code below:
numbers_a = range(1, 13)

numbers_b = []
for i in range(12):
  numbers_b.append(random.randint(1,1000))
  
plt.plot(numbers_a, numbers_b)
plt.show()
