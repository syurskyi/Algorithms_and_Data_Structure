import re

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1
STOP = ' '

def _seek_next(grid: list, position: tuple):
    row, col = position
    next_val = grid[row][col] + 1
    if row < len(grid)-1 and grid[row + 1][col] == next_val:
        return (row + 1, col), DOWN
    if row > 0 and grid[row - 1][col] == next_val:
        return (row - 1, col), UP
    if col < len(grid[row])-1 and grid[row][col + 1] == next_val:
        return (row, col + 1), RIGHT
    if col > 0 and grid[row][col - 1] == next_val:
        return (row, col - 1), LEFT
    return (row, col), STOP


def print_sequence_route(grid: str, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    grid_array = [[int(v) for v in re.findall(r'(\d+)', line)]
                  for line in grid.splitlines(keepends=False)
                  if len(line.replace('|', '').strip()) > 0]

    start_coordinates = [(row, col)
                         for row in range(len(grid_array))
                         for col in range(len(grid_array[row]))
                         if grid_array[row][col] == START_VALUE][0]

    current_direction = RIGHT
    current_vals = [str(START_VALUE)]

    this_val = START_VALUE + 1
    next_coordinates = start_coordinates
    while current_direction != STOP:
        next_coordinates, next_direction = _seek_next(grid_array, next_coordinates)
        if current_direction == next_direction:
            current_vals.append(str(this_val))
        else:
            print(f'{" ".join(current_vals)} {next_direction}')
            current_vals = [str(this_val)]
            current_direction = next_direction
        this_val += 1

    print('done')
