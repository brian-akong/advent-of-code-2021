from typing import final
from input_data import input_data

import pprint
import re

pprint = pprint.PrettyPrinter(width=1)
final_result = []

for x in input_data:
    intermediate_result = []
    converter = {
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': [],
        'f': [],
        'g': []
    }

    pipe_index = x.index('|')

    # Convert each line of input into a list (remove "|")
    scrubbed_input = x.replace("|", "")
    scrubbed_input = scrubbed_input.split()

    # consider 1
    for y in scrubbed_input:
        if len(y) == 2:
            converter['c'] = y
            converter['f'] = y

    # consider 7
    for y in scrubbed_input:
        if len(y) == 3:
            for z in y:
                if z not in converter['c'] or z not in converter['f']:
                    converter['a'] = z

    # consider 4
    for y in scrubbed_input:
        unique_segs_of_four = []
        if len(y) == 4:            
            for z in y:                
                if z not in converter['c'] or z not in converter['f']:                    
                    unique_segs_of_four.append(z)

            unique_segs_of_four = list(set(unique_segs_of_four))
            converter['b'] = "".join(unique_segs_of_four)
            converter['d'] = "".join(unique_segs_of_four)

    # consider 8
    for y in scrubbed_input:
        if len(y) == 7:
            for z in y:
                if (z not in converter['a'] and 
                    z not in converter['b'] and
                    z not in converter['c'] and
                    z not in converter['d'] and
                    z not in converter['f']
                ):
                    converter['e'].append(z)
                    converter['g'].append(z)
    converter['e'] = ''.join(set(converter['e']))
    converter['g'] = ''.join(set(converter['g']))

    # consider 9
    for y in scrubbed_input:
        if (len(y) == 6 and 
            converter['b'][0] in y and
            converter['b'][1] in y and
            converter['d'][0] in y and
            converter['d'][1] in y and
            converter['c'][0] in y and
            converter['c'][1] in y and
            converter['f'][0] in y and 
            converter['f'][1] in y
        ):
            for z in y:
                if (
                    z not in converter['b'] and
                    z not in converter['d'] and
                    z not in converter['c'] and
                    z not in converter['f'] and
                    z not in converter['a']
                ):
                    converter['g'] = z

    # Just having determined 'g', we now know 'e'
    converter['e'] = converter['e'].replace(converter['g'], '')

    # Consider 0
    for y in scrubbed_input:
        d_segment = ""
        if (len(y) == 6 and
            converter['a'] in y and
            converter['e'] in y and
            converter['c'][0] in y and
            converter['c'][1] in y and
            converter['f'][0] in y and
            converter['f'][1] in y
        ):
            d_segment = str(set(y).symmetric_difference(set('abcdefg')))
            converter['d'] = re.sub("[{}']", "", d_segment)

    # Just having determined 'd', we now know 'b'
    converter['b'] = converter['b'].replace(converter['d'], '')

    # Consider 6
    for y in scrubbed_input:
        if len(y) == 6 and converter['d'] in y and converter['e'] in y:
            for z in y:
                if (
                    z not in converter['a'] and
                    z not in converter['b'] and
                    z not in converter['d'] and
                    z not in converter['e'] and
                    z not in converter['g']
                ):
                    converter['f'] = z

    # Just having determined 'f', we now know 'c'
    converter['c'] = converter['c'].replace(converter['f'], '')                

    # Convert combos to digits
    resulting_digits = x[pipe_index + 2:].split()
    # print(f'resulting_digits = {resulting_digits}')

    for digit in resulting_digits:
        # 1, 4, 7, and 8 have unique lengths
        if len(digit) == 2:
            intermediate_result.append(1)
        elif len(digit) == 4:
            intermediate_result.append(4)
        elif len(digit) == 3:
            intermediate_result.append(7)
        elif len(digit) == 7:
            intermediate_result.append(8)
        # next check each remaining digit
        # zero
        elif converter['a'] in digit and converter['b'] in digit and converter['c'] in digit and converter['e'] in digit and converter['f'] in digit and converter['g'] in digit:
            intermediate_result.append(0)
        # six
        elif converter['a'] in digit and converter['b'] in digit and converter['d'] in digit and converter['e'] in digit and converter['f'] in digit and converter['g'] in digit:
            intermediate_result.append(6)
        # nine
        elif converter['a'] in digit and converter['b'] in digit and converter['c'] in digit and converter['d'] in digit and converter['f'] in digit and converter['g'] in digit:
            intermediate_result.append(9)
        # two
        elif converter['a'] in digit and converter['c'] in digit and converter['d'] in digit and converter['e'] in digit and converter['g'] in digit:
            intermediate_result.append(2)
        # three
        elif converter['a'] in digit and converter['c'] in digit and converter['d'] in digit and converter['f'] in digit and converter['g'] in digit:
            intermediate_result.append(3)
        # five
        elif converter['a'] in digit and converter['b'] in digit and converter['d'] in digit and converter['f'] in digit and converter['g'] in digit:
            intermediate_result.append(5)

    final_number = ''.join([str(i) for i in intermediate_result])
    final_result.append(final_number)


answer = sum([int(i) for i in final_result])
print(f'final_result: {answer}') # 🤯