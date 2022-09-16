
from functions import draw_board
from functions import check_turn
from functions import check_for_win
import os



grid = {

    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9'
}

playing = True
turn = 0
prev_turn = -1
complete = False

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(grid)

    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player" + str((turn % 2)+ 1) + "'s turn: Pick your spot or pres q to quit")

    choice = input()
    if choice == 'q':
        playing = False
    
    elif str.isdigit(choice) and int(choice) in grid:

        if not grid[int(choice)] in {"X", "O"}:

            turn += 1
            grid[int(choice)] = check_turn(turn)

    if check_for_win(grid): playing, complete = False, True
    if turn > 8: playing = False

 
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(grid)
 
if complete:
    if check_turn(turn) == 'X': print("Player 1 Wins!")
    else: print("Player 2 Wins!")
else:
    print("No Winner.")

print("Thanks for playing!")
