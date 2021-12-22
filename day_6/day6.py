from typing import final
from example_data import input_data
import copy

class LanternFish():
    def __init__(self, internal_timer=8):
        self.internal_timer = internal_timer

    def reproduce(self):
        return LanternFish()

    def live(self):
        if self.internal_timer == 0:
            self.internal_timer = 6
        else:
            self.internal_timer -= 1

def create_fish(internal_timer):
    return LanternFish(internal_timer)

initial_fish_population = []
for fish in input_data:
    initial_fish_population.append(create_fish(fish))

# duration = 256
duration = 2
for i in range(1, duration + 1):
    fish_population = len(initial_fish_population)
    for x in range(fish_population):
        fish = initial_fish_population[x]
        if fish.internal_timer == 0:
            fish.live()
            new_fish = fish.reproduce()
            initial_fish_population.append(new_fish)
        else:
            fish.live()
    age_list = []
    # for f in initial_fish_population:
    #     age_list.append(f.internal_timer)
    # print(f'timers after {i} days: {age_list}')

def create_lantern_fish(internal_timer=8):
    return {'internal_timer': internal_timer}

def reproduce(population, age):
    if age == 0:
        population.append(8)
        return 6
    return age - 1

result = len(input_data)
i = 1

number_of_days = int(input("Enter number of days: ")) # enter in 256
while i <= number_of_days:
    population_size = len(input_data)
    for index in range(population_size):
        if input_data[index] == 0:
            result += (number_of_days - index) / 7
            input_data.append(8)
        else:
            input_data[index] -= 1
    # for f in input_data:
    #     age_list.append(f)
    # print(f'timers after {i} days: {input_data}')
    i += 1

for index, fish in enumerate(input_data):    
    result += (number_of_days - fish) / 7

print(len(input_data))

# print(f'Number of lantern fish after 80 days: {len(initial_fish_population)}')
# print(f'Number of lantern fish after {duration} days: {len(initial_fish_population)}')

# 26984457539 expected
# 2621894
# ___ actual