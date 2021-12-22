from input_data import input_data

import pprint

count = 0
for x in input_data:
    # print(x, sep="/n")
    converter = {
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': [],
        'f': [],
        'g': []
    }

    index = x.index('|')

    input = x[index + 1:]
    arr = input.split(' ')
    # for idx, i in enumerate(arr)
    # print(arr)

    for y in arr:
        print(y)
        if len(y) == 2 or len(y) == 4 or len(y) == 3 or len(y) == 7:
            count += 1


print(input_data)
pprint.pprint(count)