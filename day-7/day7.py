from input_data import input_data
from statistics import mean

def sum_fuel(n):
    return sum(range(1, n + 1))

fuel_counts = []
for index, element in enumerate(range(len(input_data) + 1)):
    fuel_count = 0
    for element in input_data:
        fuel_count += sum_fuel(abs(index - element))
    fuel_counts.append(fuel_count)

print(min(fuel_counts))