
def find_battleship(grid_size: int):
    for r in range(grid_size):
        for c in range(grid_size):
            if bomb_location(r, c):  # first hit
                cells = [(r, c)]

                # check right (horizontal case)
                if c + 1 < grid_size and bomb_location(r, c+1):
                    cells.append((r, c+1))
                    if c + 2 < grid_size and bomb_location(r, c+2):
                        cells.append((r, c+2))
                    return cells

                # check down (vertical case)
                if r + 1 < grid_size and bomb_location(r+1, c):
                    cells.append((r+1, c))
                    if r + 2 < grid_size and bomb_location(r+2, c):
                        cells.append((r+2, c))
                    return cells

                # If ship is centered on the first hit, check both directions
                if c - 1 >= 0 and bomb_location(r, c-1):
                    cells.append((r, c-1))
                if r - 1 >= 0 and bomb_location(r-1, c):
                    cells.append((r-1, c))

                return sorted(cells)
