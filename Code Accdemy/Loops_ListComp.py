heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)


celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [c * 9/5 + 32 for c in celsius]

print(fahrenheit)
