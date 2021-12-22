from raw_data import input_data

element_length = len(input_data[0])

output = []
for x in range(element_length):
    output.append(0)

for binary in input_data:
    for index, character in enumerate(binary):
        if character == "0":
            output[index] = output[index] - 1
        else:
            output[index] = output[index] + 1

gamma = ""
epsilon = ""
for character in output:
    if character > 0:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"

def binaryToDecimal(binary):
    binary = int(binary)
    binary2 = binary
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
    

gamma_decimal = binaryToDecimal(gamma)
epsilon_decimal = binaryToDecimal(epsilon)

print(f'gamma = {gamma}; gamma in decimal = {gamma_decimal}')
print(f'gamma = {epsilon}; gamma in decimal = {epsilon_decimal}')
print(f'Final answer: {gamma_decimal} * {epsilon_decimal} = {gamma_decimal * epsilon_decimal}')
