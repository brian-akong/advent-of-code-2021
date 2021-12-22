import re
from input_data import instructions

forward = 0
aim = 0
depth = 0

def find_number(instruction):
    number_list = re.findall(r'\d+', instruction)
    final_number = sum(map(int, number_list))
    return final_number

for x in instructions:
    if 'forward' in x:    
        increment = find_number(x)
        forward += increment
        if aim > 0:
            depth += aim * increment
    elif 'down' in x:
        increment = find_number(x)        
        aim += increment
    elif 'up' in x:
        increment = find_number(x)        
        aim -= increment

print(f'forward = {forward}')
print(f'depth = {depth}')
print(f'FINAL ANSWER OF forward * depth = {forward * depth}')