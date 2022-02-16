vehicles = [{'type': 'Sedan', 'weight': 1500, 'year': 2000}, {'type': 'SUV', 'weight': 2000, 'year': 1999},
            {'type': 'Pickup', 'weight': 2500, 'year': 2011}, {'type': 'Minivan', 'weight': 1600, 'year': 1999},
            {'type': 'Van', 'weight': 2400, 'year': 2012}, {'type': 'Semi', 'weight': 13600, 'year': 2015},
            {'type': 'bycicle', 'weight': 7, 'year': 2012}, {'type': 'Motocycle', 'weight': 100, 'year': 2008}]
sorted_by_key = sorted(vehicles, key=lambda k: k['type'])
sorted_by_value_of_k = sorted(vehicles, key=lambda v: v['year'])
print(sorted_by_value_of_k)



