first_names = ["Ainsley", "Ben", "Chani", "Depak"]
age = []
age.append(42)
all_ages = age + [32, 41, 29]

name_and_age = zip(first_names,all_ages)
ids = range(4)

name_and_age_and_id = zip(first_names, all_ages, ids)

print(list(name_and_age_and_id))
