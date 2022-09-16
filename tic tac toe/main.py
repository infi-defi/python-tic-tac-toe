#Γινοταν κολος με τις γραμμες για αυτο τα fuctions τα κανω import απο το αλλο αρχειο
from functions import draw_board
from functions import check_turn
from functions import check_for_win
import os #goofy ahh library ig?


# Εδω με λιγα λογια αντοιστοιχει το καθε νουμερο με ενα value. Δλδ αν οταν διαλεγει ο παιχτης τι να παιξει
# πει "1" τοτε θα μεταφρασει το "1" σε 1 θα ψαξει που στον πινακα (το draw_board) που ειναι το 1 και μετα 
# θα το αντοικαταστησει με X ή Ο ανοιστηχα
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
    # Εδω καθαρηζεο την οθονη (το cls ειναι για το αν εισαι σε windows. 
    # Αλιως κανει clear αν εισαι σε ορθοδωξα linux).
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(grid)

    # Λεει αν καποιος εκανε μια ακυρη κινηση. Αλιως λεει τον επομενο παιχτη να παιξει.
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player" + str((turn % 2)+ 1) + "'s turn: Pick your spot or pres q to quit")

    # Εδω περνει input απο τους players
    choice = input()
    if choice == 'q':
        playing = False
    
    # Jesus. Λοιπον η λογικη πισω απο αυτο ειναι οτι θα αλαξουμε τον πινακα μονο αν το input περναει
    # απο καποια συγκεκριμενα conditions. Αρχικα πρεπει να βεβαιοθουμε οτι input ειναι intigure thingy.
    # Το "str.isdigit(choice)" κανει οτι λεει. Κοιταει αν το input ειναι digit.
    # Και επειδη θελουμε η απαντηση να ειναι μεσα στο grid (δλδ απο το 1-9) το "int(choice) in grid" ελενχει
    # αν η απαντηση του παιχτη ειναι κατι που υπαρχει στο grid
    elif str.isdigit(choice) and int(choice) in grid:

    # Ελενχει αν εκεινη η θεση ειναι πιασμενη. Κυριολεκτικα απλα αυτο.Βλεπει αν το choice != με Χ ή Ο. 
    # Αν εινια συνεχιζει με την ζωη του
        if not grid[int(choice)] in {"X", "O"}:
    
    # Oh boy. Αν και τα δυο απο πανω ισχιουν τοτε ξερουμε οτι ο παιχτης μας εδωσε ενα valid input.
    # Αρα θα αυξανουμε την γυρα κατα 1
    # Και θα αλαξουμε την επιθημιτη θεση στον πινακα με X ή O αναλογα με την γυρα.
    # Το "grid[int(choice)] = check_turn(turn)" περνει το choice ας πουμε οτι ειναι 4. 
    # Το κανει int και μετα δλδ καταληγουμε με ενα "grid[4] = check_turn(turn)". 
    # Ταυτοχρονα το check_turn βλεπει τι γυρα ειναι ας πουμε 4 και διαλεγει αν θα παιξει ο X ή ο O . 
    # Σε αυτη την περιπτωησ θα παιξει ο Ο. Αρα μετα καταληγουμε με grid[4] = O που αλαζει το grid[4] με ενα O
            turn += 1
            grid[int(choice)] = check_turn(turn)

    # Check αν εχει τελειωσει το παιχνιδι ή αν καποιος νικησε
    if check_for_win(grid): playing, complete = False, True
    if turn > 8: playing = False

# Φτιαξε το board μια τελευταια φορα . 
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(grid)

# Αν υπαρχει νικιτης πες ποιος νικησε. 
if complete:
    if check_turn(turn) == 'X': print("Player 1 Wins!")
    else: print("Player 2 Wins!")
else:
    # Ισοπαλια
    print("No Winner.")

print("Thanks for playing!")