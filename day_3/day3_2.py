import copy
from raw_data import input_data

oxygen = copy.deepcopy(input_data)
co2 = copy.deepcopy(input_data)

element_length = len(oxygen[0])

output = []
for x in range(element_length):
    output.append(0)

for x in range(element_length):
    if (len(oxygen) == 1):
        break
    for binary in oxygen:
        if binary[x] == "0":
            output[x] = output[x] - 1
        else:
            output[x] = output[x] + 1
    length_oxygen = len(oxygen)
    oxygen_removable = []
    for ind in range(length_oxygen):
        if output[x] < 0 and oxygen[ind][x] == "1":
           oxygen_removable.append(oxygen[ind])
        elif output[x] >= 0 and oxygen[ind][x] == "0":
           oxygen_removable.append(oxygen[ind])
    for item in oxygen_removable:
        oxygen.remove(item)

print (oxygen[0])

output2 = []
for x in range(element_length):
    output2.append(0)

for x in range(element_length):
    if (len(co2) == 1):
        break
    for binary2 in co2:
        if binary2[x] == "0":
            output2[x] = output2[x] - 1
        else:
            output2[x] = output2[x] + 1
    length_co2 = len(co2)
    co2_removable = []
    for ind in range(length_co2):
        if output2[x] >= 0 and co2[ind][x] == "1":
           co2_removable.append(co2[ind])
        elif output2[x] < 0 and co2[ind][x] == "0":
           co2_removable.append(co2[ind])
    for item in co2_removable:
        co2.remove(item)

print(co2[0])
print (781 * 2734)

# 001100001101
# 101010101110
# 2135254