from input_data import input_data as grid
import pprint

grid = [list(x) for x in grid]

total_flashes = 0

def make_list_flat(input_list):
    return [int(item) for sublist in input_list for item in sublist]

def incremenet_all_elements():
    for idx_y, y in enumerate(grid):
        for idx_x, x in enumerate(y):
            grid[idx_x][idx_y] = int(grid[idx_x][idx_y]) + 1

def increment_from_flash(x_index, y_index):
    if y_index - 1 >= 0: # top
        grid[y_index - 1][x_index] = grid[y_index - 1][x_index] + 1

    if y_index - 1 >= 0 and x_index + 1 < len(grid[y_index]): # diagonal top right
        grid[y_index -1][x_index + 1] = grid[y_index - 1][x_index + 1] + 1

    if x_index + 1 < len(grid[y_index]): # right
        grid[y_index][x_index + 1] = grid[y_index][x_index + 1] + 1

    if y_index + 1 < len(grid) and x_index + 1 < len(grid[y_index]): # diagonal bottom right
        grid[y_index + 1][x_index + 1] = grid[y_index + 1][x_index + 1] + 1

    if y_index + 1 < len(grid): # bottom
        grid[y_index + 1][x_index] = grid[y_index + 1][x_index] + 1

    if y_index + 1 < len(grid) and x_index - 1 >= 0: # diagonal bottom left
        grid[y_index + 1][x_index -1] = grid[y_index + 1][x_index - 1] + 1

    if x_index - 1 >= 0: # left
        grid[y_index][x_index -1] = grid[y_index][x_index - 1] + 1

    if y_index -1 >= 0 and  x_index - 1 >= 0: # diagonoal top left
        grid[y_index - 1][x_index -1] = grid[y_index - 1][x_index - 1] + 1


def check_for_flashes():
    flash_count = 0
    for idx_y, y in enumerate(grid):
        for idx_x, x in enumerate(y):
            if grid[idx_y][idx_x] > 9:
                grid[idx_y][idx_x] = 0
                zeros.append((idx_x, idx_y))
                flash_count += 1
    return flash_count


# incremenet_all_elements()
# print(sum(make_list_flat(grid)))

def set_to_zero_after_flash(x_index, y_index):
    grid[y_index][x_index] = 0

zeros = []
synchronization_steps = []

for i in range(500):
    zeros = []
    incremenet_all_elements()

    total_flashes += check_for_flashes()

    # Now consider flashes from chain reaction of flashes
    for item in zeros:
        x_index, y_index = item
        grid[y_index][x_index] = 0
        increment_from_flash(x_index, y_index)
        total_flashes += check_for_flashes()

    for pair in zeros:
        x_index, y_index = pair
        set_to_zero_after_flash(x_index, y_index)

    if sum(make_list_flat(grid)) == 0:
        print(f'Total synchonization occurred on step {i + 1}!')
        synchronization_steps.append(i)



# pprint.pprint(grid)
print(f'total_flashes = {total_flashes}')
print(f'Synchronization occured on steps {synchronization_steps}')
# 385 too low