from random import choice

def generate_grid():
    '''
    Generates an empty grid to play with
    '''
    grille = [[0 for j in range(4)] for i in range(4)]
    add_random_tile(grille)
    add_random_tile(grille)
    return grille

def addition_compatible(nb1, nb2):
    '''
    Checks if two number (nb1 & nb2) can be added/combined (eg: 2 and 2, 16 and 16, but not 8 with 64)
    '''
    return nb1 == nb2 and nb1 != 0

def wanted_direction():
    '''
    Returns the direction chosen by the player
    '''
    mov = ['u', 'r', 'l', 'd'] #up, right, left, down
    print("Press U for UP, D for DOWN, R for RIGHT and L for LEFT.")
    key_pressed = input().lower()
    while key_pressed not in mov:
        print("Invalid key. It must be U or D or R or L.")
        key_pressed = input().lower()
    return {'r': 'right', 'l': 'left', 'u': 'up', 'd': 'down'}[key_pressed]

def slide_row(row):
    """
    Slides and combines a row (to the left)
    """
    new_row = [num for num in row if num != 0]
    for i in range(len(new_row) - 1):
        if addition_compatible(new_row[i], new_row[i + 1]):
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [num for num in new_row if num != 0]
    return new_row + [0] * (4 - len(new_row))

def slide_left(grille):
    """Applique le mouvement vers la gauche sur toute la grille."""
    return [slide_row(row) for row in grille]

def slide_right(grille):
    """Applique le mouvement vers la droite sur toute la grille."""
    return [slide_row(row[::-1])[::-1] for row in grille]

def slide_up(grille):
    """Applique le mouvement vers le haut."""
    transposed = list(zip(*grille))
    slid = slide_left([list(row) for row in transposed])
    return [list(row) for row in zip(*slid)]

def slide_down(grille):
    """Applique le mouvement vers le bas."""
    transposed = list(zip(*grille))
    slid = slide_right([list(row) for row in transposed])
    return [list(row) for row in zip(*slid)]

def add_random_tile(grille):
    """Ajoute une tuile 2 ou 4 aléatoirement dans une case vide."""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grille[i][j] == 0]
    if not empty_cells:
        return
    i, j = choice(empty_cells)
    grille[i][j] = choice([2, 4])

def print_grid(grille):
    """Affiche la grille."""
    for row in grille:
        print("\t".join(str(num).rjust(4) if num != 0 else ".".rjust(4) for num in row))
    print()

def is_game_over(grille):
    """Vérifie si le jeu est terminé."""
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 0:
                return False
            if j < 3 and addition_compatible(grille[i][j], grille[i][j + 1]):
                return False
            if i < 3 and addition_compatible(grille[i][j], grille[i + 1][j]):
                return False
    return True

def two_zero_four_eight_game():
    """Lance le jeu."""
    grille = generate_grid()
    print("Bienvenue dans le jeu 2048 !")
    print_grid(grille)

    while True:
        direction = wanted_direction()
        if direction == "left":
            new_grille = slide_left(grille)
        elif direction == "right":
            new_grille = slide_right(grille)
        elif direction == "up":
            new_grille = slide_up(grille)
        else:  # down
            new_grille = slide_down(grille)
        if new_grille != grille:
            grille = new_grille
            add_random_tile(grille)
        else:
            print("Mouvement impossible. Choisissez une autre direction.")

        print_grid(grille)

        if is_game_over(grille):
            print("Game Over! Merci d'avoir joué.")
            break