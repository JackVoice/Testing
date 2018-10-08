def ground_ship(weight):
  cost = 20
  if weight > 10:
    cost += 4.75 * weight
  elif weight > 6:
    cost += 4 * weight
  elif weight > 2:
    cost += 3 * weight
  elif weight <= 2:
    cost += 1.5 * weight
  else:
    return "Something has gone wrong"
  return round(cost,2)

print(ground_ship(1))
print(ground_ship(4))
print(ground_ship(8.4))
print(ground_ship(22))

prem_ship = 125

def drone_ship(weight):
  cost = 0
  if weight > 10:
    cost += 14.25 * weight
  elif weight > 6:
    cost += 12 * weight
  elif weight > 2:
    cost += 9 * weight
  elif weight <= 2:
    cost += 4.5 * weight
  else:
    return "Something has gone wrong"
  return round(cost,2)

print(drone_ship(1.5))
print(drone_ship(4))
print(drone_ship(8.4))
print(drone_ship(22))

def cheap_ship(weight):
  if prem_ship < ground_ship(weight) and prem_ship < drone_ship(weight):
  	return "Premium Shipping at a cost of $" + str(prem_ship)
  elif ground_ship(weight) >= drone_ship(weight):
    return "Drone Shipping at a cost of $" + str(drone_ship(weight))
  else:
    return "Ground Shipping at a cost of $" + str(ground_ship(weight))

print(cheap_ship(4.8))
