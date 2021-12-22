from input_data import input_data as height_map

row_length = len(height_map[0])
number_of_rows = len(height_map)

def check_corner(corner, first_edge, second_edge):
    if first_edge > corner and second_edge > corner:
        return corner

def check_edge(edge, first_edge, second_edge, third_edge):
    if first_edge > edge and second_edge > edge and third_edge > edge:
        return edge

def check_four_neighbors(point, top_neighbor, right_neighbor, bottom_neighbor, left_neighbor):
    if (
        top_neighbor > point and
        right_neighbor > point and
        bottom_neighbor > point and
        left_neighbor > point
    ):
        return point    

low_points = []

for row_index, row in enumerate(height_map):
    for element_index, point in enumerate(row):
        location = height_map[row_index][element_index]
        # top left corner
        if row_index == 0 and element_index == 0:
            result = check_corner(location, height_map[0][1], height_map[1][0])
            if result is not None:
                low_points.append(location)
        # top right corner
        elif row_index == 0 and element_index == row_length - 1:
            result = check_corner(location, height_map[0][row_length - 2], height_map[1][row_length - 1])
            if result is not None:
                low_points.append(location)
        # bottom left corner
        elif row_index == number_of_rows - 1 and element_index == 0:
            result = check_corner(location, height_map[number_of_rows - 2][0], height_map[number_of_rows - 1][1])
            if result is not None:
                low_points.append(location)
        # bottom right corner
        elif row_index == number_of_rows - 1 and element_index == row_length - 1:
            result = check_corner(location, height_map[number_of_rows - 2][row_length - 2], height_map[number_of_rows - 1][row_length - 2])
            if result is not None:
                low_points.append(location)
        # first row edges
        elif row_index == 0:
            result = check_edge(location, height_map[0][element_index - 1], height_map[0][element_index + 1], height_map[1][element_index])
            if result is not None:
                low_points.append(location)
        # bottom row edges
        elif row_index == number_of_rows - 1:
            result = check_edge(location, height_map[number_of_rows - 1][element_index - 1], height_map[number_of_rows - 1][element_index + 1], height_map[number_of_rows - 2][element_index])
            if result is not None:
                low_points.append(location)
        # left column edges
        elif element_index == 0:
            result = check_edge(location, height_map[row_index - 1][element_index], height_map[row_index][element_index + 1], height_map[row_index + 1][element_index])
            if result is not None:
                low_points.append(location)
        # right column edges
        elif element_index == row_length - 1:
            result = check_edge(location, height_map[row_index + 1][element_index], height_map[row_index][element_index - 1], height_map[row_index - 1][element_index])
            if result is not None:
                low_points.append(location)
        # all other locations
        else:
            result = check_four_neighbors(location, height_map[row_index - 1][element_index], height_map[row_index][element_index + 1], height_map[row_index + 1][element_index], height_map[row_index][element_index - 1])
            if result is not None:
                low_points.append(location)
                

print(f'low_points: {low_points}')


risk_levels = [int(low_point) + 1 for low_point in low_points]
print(f'risk_levels: {risk_levels}')
print(f'Total risk: {sum(risk_levels)}')