

def draw_board(grid):
    board = (f"|{grid[1]}|{grid[2]}|{grid[3]}|\n"
                f"|{grid[4]}|{grid[5]}|{grid[6]}|\n"
                f"|{grid[7]}|{grid[8]}|{grid[9]}|")
    print(board)

def check_turn(turn):
    return 'O' if not (turn % 2) else 'X'    


def check_for_win(grid):
    if  (grid[1] == grid[2] == grid[3]) \
        or (grid[4] == grid[5] == grid[6]) \
        or (grid[7] == grid[8] == grid[9]):
        return True
    if  (grid[1] == grid[4] == grid[7]) \
        or (grid[2] == grid[5] == grid[8]) \
        or (grid[3] == grid[6] == grid[9]):
        return True
    if  (grid[1] == grid[5] == grid[9]) \
        or (grid[3] == grid[5] == grid[7]):
        return True
    else: return False
