"""
Consider a square grid of size N, where N>=3. I have placed a battleship of #size 3 somewhere in the grid,
and you want to sink-my battleship by ordering the bombing of specified coordinates.

The battleship can only be placed vertically or horizontally, not diagonally.
Every coordinate which does not contain the battleship is empty.Your task is to write a function 
which takes as input N, and returns the 3 coordinates of the battleship.

Assume you have a function, boolean bomb_location(x, y) which will return True if (x, y) "hits" the battleship 
and False if (x, y) misses the battleship.

For example - in the following grid your function find_battleship(grid_size), 
given grid_size of 8, would return ( (2,1), (2, 2), (2,3)) :
    . . . . . . . .
    . . X . . . . .
    . . X . . . . .
    . . X . . . . .
    . . . . . . . .
    . . . . . . . .
    . . . . . . . . 
    . . . . . . . .
"""
class Solution:
    def findBattleShip(self, N):
        hits = []
        
        # Phase 1: Find any 3 cells that belong to the battleship
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                if bomb_location(r, c):  # This function is provided by the judge
                    hits.append((r, c))
                if len(hits) == 3:
                    break
            if len(hits) == 3:
                break
        
        # We now have 3 hit coordinates
        (r1, c1), (r2, c2), (r3, c3) = hits

        # Determine orientation
        if r1 == r2 == r3:
            # Horizontal ship
            row = r1
            cols = sorted([c1, c2, c3])
            return ((row, cols[0]), (row, cols[1]), (row, cols[2]))
        else:
            # Vertical ship
            col = c1
            rows = sorted([r1, r2, r3])
            return ((rows[0], col), (rows[1], col), (rows[2], col))


# Example of how the judge might test it (you can't run this locally without the API)
# But for understanding:
def bomb_location(r, c):
    ship = [(2,1), (2,2), (2,3)]
    return (r, c) in ship

# Test
if __name__ == "__main__":
    sol = Solution()
    result = sol.findBattleShip(8)  # N= 8, for example
    print(result)  # Expected: ((2, 1), (2, 2), (2, 3))
