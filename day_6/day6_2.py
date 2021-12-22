from input_data import input_data
from collections import defaultdict

mydict = defaultdict(int)

for n in input_data:
    if n not in mydict:
        mydict[n] = 0
    mydict[n] +=1

for day in range(256):
    y = defaultdict(int)
    for x, cnt in mydict.items():
        if x == 0:
            y[6] += cnt
            y[8] += cnt
        else:
            y[x-1] += cnt
    mydict = y

print(sum(mydict.values()))