from input_data import input_data as source_code
import re
import copy
import statistics

opening_characters = ["(", "[", "{", "<"]
closing_characters = [")", "]", "}", ">"]
all_pairs = [opener+closer for opener in opening_characters for closer in closing_characters]
valid_pairs = ["()", "[]", r"{}", "<>"]

refined_lines = []
score = 0

for line in source_code:
    while (
        "()" in line or 
        "[]" in line or
        "{}" in line or
        "<>" in line
    ):
        line = re.sub("\(\)|\[\]|\{\}|<>", "", line)
    refined_lines.append(line)

for line in refined_lines:
    # Iterate through all_pairs and find the first INvalid pair in the line
    # Find the invalid character and calculate a score
    for pair in all_pairs:
        if pair in line:
            print(f'Found a bad pair! -> {pair}')
            if pair[-1] == ')':
                score += 3
            elif pair[-1] == ']':
                score += 57
            elif pair[-1] == '}':
                score += 1197
            elif pair[-1] == '>':
                score += 25137

print(f"Syntax score: {score}")

# Part 2
incomplete_lines = copy.deepcopy(refined_lines)

for idx, line in enumerate(incomplete_lines):
    for pair in all_pairs:
        if pair in line:
            incomplete_lines.remove(line)
            incomplete_lines = copy.deepcopy(incomplete_lines) # eww

def calculate_autocomplete_score_per_line(sequence):
    score = 0
    for char in sequence:
        if char == ')':
            score = score * 5 + 1
        elif char == ']':
            score = score * 5 + 2
        elif char == '}':
            score = score * 5 + 3
        elif char == '>':
            score = score * 5 + 4
    return score
  
auto_complete_scores = []
for line in incomplete_lines:
    closing_characters = ''
    # Starting from the right-most character, find its corresponding closing character
    for char in reversed(line):
        if char == '(':
            closing_characters += ')'
        elif char == '[':
            closing_characters += ']'
        elif char == '{':
            closing_characters += '}'
        elif char == '<':
            closing_characters += '>'
    # print(f'closing_characters: {closing_characters} | Score: {calculate_autocomplete_score_per_line(closing_characters)}')
    auto_complete_scores.append(calculate_autocomplete_score_per_line(closing_characters))

print(f'Middle score: {statistics.median(auto_complete_scores)}')
