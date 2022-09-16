# Εδω φτιαχνει/ζωγραφιζει τον πινακα. Βαση με το dictionary(το grid) στο main.py βαζει τις γραμμες "|" και
# μετα βαζει μεσα το αντοιστηχο νουμερο(πχ: η θεση 1 = {grid[1]}.Αλλα αυτο στο τελος απλα φενεται σαν 1).

def draw_board(grid):
    board = (f"|{grid[1]}|{grid[2]}|{grid[3]}|\n"
                f"|{grid[4]}|{grid[5]}|{grid[6]}|\n"
                f"|{grid[7]}|{grid[8]}|{grid[9]}|")
    print(board)


# Εδω αποφασιζει ποιανου ειναι η σειρα αν ειναι μονα ή ζηγα. 
# Με λιγα λογια αν ο αριθμος της γυρας μπορει να διερεθει με το 2 χωρις υπολοιπο τοτε παιζει ο 'O' αλιως ο 'X'. 
# Αν πχ ειναι η τριτη γυρα τοτε 3/2 εχει υπολοιπο 1 αρα παιζουν τα Χ. Αν εινια η γυρα 12 τοτε 12/2 
# εχει υπολοιπο O αρα παιζουν τα O
def check_turn(turn):
    return 'O' if not (turn % 2) else 'X'    


# Βλεπει αν καποιος εχει νικησει
def check_for_win(grid):
    # οριζοντια
    if  (grid[1] == grid[2] == grid[3]) \
        or (grid[4] == grid[5] == grid[6]) \
        or (grid[7] == grid[8] == grid[9]):
        return True
    # καθετα
    if  (grid[1] == grid[4] == grid[7]) \
        or (grid[2] == grid[5] == grid[8]) \
        or (grid[3] == grid[6] == grid[9]):
        return True
    # διαγωνια
    if  (grid[1] == grid[5] == grid[9]) \
        or (grid[3] == grid[5] == grid[7]):
        return True
    else: return False