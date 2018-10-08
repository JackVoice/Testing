dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for i in dog_breeds_available_for_adoption:
  print(i)
  if i == dog_breed_I_want:
    print("They have the dog I want!")
    break
