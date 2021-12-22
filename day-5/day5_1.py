from input_data import coordinates
import copy

filtered_coordinates = []
grid = []
x_rows = []

print(len(coordinates))

# Filter out non-horizontal and non-vertical lines
for coordinate_set in coordinates:
    if coordinate_set[0][0] == coordinate_set[1][0] or coordinate_set[0][1] == coordinate_set[1][1]:
        filtered_coordinates.append(coordinate_set)

def find_maximum_coordinates(list_of_coordinates):
    x_axis_maximum = 0
    y_axis_maximum = 0
    for coordinate_set in list_of_coordinates:
        for pair in coordinate_set:
            if pair[0] > x_axis_maximum:
                x_axis_maximum = pair[0]
            if pair[1] > y_axis_maximum:
                y_axis_maximum = pair[1]
    return (x_axis_maximum, y_axis_maximum)

# Build grid
x_max, y_max = find_maximum_coordinates(filtered_coordinates)
for x in range(x_max + 1):
    x_rows.append(0)

for y in range(y_max + 1):
    new_x_row = copy.deepcopy(x_rows)
    grid.append(new_x_row)

def mark_grid(grid, list_of_coordinates):
    for coordinate_set in list_of_coordinates:
        if coordinate_set[0][1] == coordinate_set[1][1]: # y1 == y2 case
            row_index = coordinate_set[0][1]
            x_start = min(coordinate_set[0][0], coordinate_set[1][0])
            x_end = max(coordinate_set[0][0], coordinate_set[1][0])
            for x in range(x_start, x_end + 1):          
                grid[row_index][x] += 1
        elif coordinate_set[0][0] == coordinate_set[1][0]: # x1 == x2 case
            column_index = coordinate_set[0][0]
            y_start = min(coordinate_set[0][1], coordinate_set[1][1])
            y_end = max(coordinate_set[0][1], coordinate_set[1][1])
            for y in range(y_start, y_end + 1):
                grid[y][column_index] += 1

mark_grid(grid, filtered_coordinates)

overlapping_points = 0
for row in grid:
    for item in row:
        if item > 1:
            overlapping_points += 1

print(f'final answer for part 1: overlapping_points = {overlapping_points}')

# PART 2
# Re-build grid
grid = []
x_rows = []
for x in range(x_max + 1):
    x_rows.append(0)

for y in range(y_max + 1):
    new_x_row = copy.deepcopy(x_rows)
    grid.append(new_x_row)

def slope_calculator(coordinate_set):
    p1 = coordinate_set[0]
    p2 = coordinate_set[1]
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    if abs((p2[1] - p1[1]) / (p2[0] - p1[0])) == 1:
        return int(slope)

part_2_coordinates = []
for coordinate_set in coordinates:
    if coordinate_set[0][0] == coordinate_set[1][0] or coordinate_set[0][1] == coordinate_set[1][1] or abs(slope_calculator(coordinate_set)) == 1:
        part_2_coordinates.append(coordinate_set)

def mark_grid_with_diagonals(grid, list_of_coordinates):
    for coordinate_set in list_of_coordinates:
        if coordinate_set[0][1] == coordinate_set[1][1]: # y1 == y2 case
            row_index = coordinate_set[0][1]
            x_start = min(coordinate_set[0][0], coordinate_set[1][0])
            x_end = max(coordinate_set[0][0], coordinate_set[1][0])
            for x in range(x_start, x_end + 1):          
                grid[row_index][x] += 1
        elif coordinate_set[0][0] == coordinate_set[1][0]: # x1 == x2 case
            column_index = coordinate_set[0][0]
            y_start = min(coordinate_set[0][1], coordinate_set[1][1])
            y_end = max(coordinate_set[0][1], coordinate_set[1][1])
            for y in range(y_start, y_end + 1):
                grid[y][column_index] += 1
        else: # diagonal case
            p1_x = coordinate_set[0][0]
            p1_y = coordinate_set[0][1]
            p2_x = coordinate_set[1][0]
            p2_y = coordinate_set[1][1]

            slope_value = abs(slope_calculator(coordinate_set))

            while (p1_x != p2_x and p1_y != p2_y):
                grid[p1_y][p1_x] += 1
                if p1_x < p2_x:
                    p1_x += slope_value
                else:
                    p1_x -= slope_value
                if p1_y < p2_y:
                    p1_y += slope_value
                else:
                    p1_y -= slope_value
            grid[p2_y][p2_x] += 1            

mark_grid_with_diagonals(grid, part_2_coordinates)

overlapping_points = 0
for row in grid:
    for item in row:
        if item > 1:
            overlapping_points += 1
print(f'final answer for part 2: overlapping_points = {overlapping_points}')