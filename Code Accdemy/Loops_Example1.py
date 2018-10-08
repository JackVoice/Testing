hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0 

for i in prices:
  total_price += i

average_price = round(total_price / len(prices),2)
print("Average Haircut Price: " + str(average_price))

new_prices = []
for i in range(len(prices)):
  new_prices.append(prices[i] - 5)
  
print(new_prices)

total_rev = 0
for i in range(len(hairstyles)):
	total_rev += prices[i] * last_week[i]
  
print("Total Revenue: " + str(total_rev))

average_daily_rev = total_rev / 7
print(average_daily_rev)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles) - 1) if new_prices[i] < 30 ]

print(cuts_under_30)
