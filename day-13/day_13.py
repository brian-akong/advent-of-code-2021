from input_data import input_data as dots
import copy
import pprint
import itertools

dots = [x.split(',') for x in dots]

x_coordinates = []
y_coordinates = []

for pair in dots:
    x_coordinates.append(int(pair[0]))
    y_coordinates.append(int(pair[1]))

x_max = max(x_coordinates)
y_max = max(y_coordinates)

grid = []
row = []
for x in range(x_max + 1):
    row.append('-')
        
for y in range(y_max + 1):
    new_row = copy.deepcopy(row)
    grid.append(new_row)

for pair in dots:
    grid[int(pair[1])][int(pair[0])] = "#"

def fold_along_x(x_fold):
    for x in range(x_fold, len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == "#" and x > x_fold:
                grid[y][x] = "-"
                grid[y][x_fold - (x - x_fold)] = "#"
    for row in grid:
        del row[x_fold:]

def fold_along_y(y_fold):
    y_max = len(grid)
    x_max = len(grid[0])
    for y in range(y_fold, y_max):
        for x in range(x_max):
            if grid[y][x] == "#" and y > y_fold:
                grid[y][x] = "-"
                grid[y_fold - (y - y_fold)][x] = "#"
    del grid[y_fold:]

fold_along_x(655)
fold_along_y(447)
fold_along_x(327)
fold_along_y(223)
fold_along_x(163)
fold_along_y(111)
fold_along_x(81)
fold_along_y(55)
fold_along_x(40)
fold_along_y(27)
fold_along_y(13)
fold_along_y(6)

# fold_along_y(7)
# fold_along_x(5)

# smalles folds
# y = 6
# x = 40

# pprint.pprint(f'Number of point: {sum(itertools.chain(*grid))}')

# pprint.pprint(grid)

for line in grid:
    print(" ".join(map(str, line)))