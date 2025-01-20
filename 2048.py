# Jeu de base -> jeu sur discord
# ===> def discord_emojis(grille) -> grille
# IN : grille (tableau 2D, la grille avec tous les nombres)
# OUT : grille (tableau 2D, la grille avec des émojis discord à la place des nombres) 

'''Why not putting the while game in a class?
This will be useful to be able to play multiple parties at the same time, allowing more than 1 person to play at the same moment'''



'''
JEU DE BASE
''' 

def addition_compatible(nb1, nb2):
    # IN : nb1 (int), nb2 (int)
    # OUT : bool
    # Checks if two number can be added/combined (eg: 2 and 2, 16 and 16, but not 8 with 64)
    if nb1 == nb2:
        return True
    return False

def wanted_direction():
    # IN : none
    # OUT : direction (str)
    # Returns the direction chosen by the player
    # ADD A WHILE TO SECURE THE INPUT
    key_pressed = input()
    if key_pressed == <right key>:
        direction = "right"
    elif key_pressed == <left key>:
        direction = "left"
    elif key_pressed == <up key>:
        direction = "up"
    else:
        direction = "bottom"
    return direction 

def add_numbers(grille):
    # IN : grille ()
    # OUT : grille ()
    # Modifies the inputed grille so that it actualises
    way = wanted_direction()
    if way == "right":
        pass
    elif way == "left":
        pass
    elif way == "up":
        pass
    else:
        pass

'''
DISCORD VERSION
''' 

def discord_emojis(grille):
    dico_emojis = {2:"number_2", 4:"number_4", 8:"number_8", 16:"number_16", 32:"number_32", 64:"number_64", 128:"number_128", 256:"number_256"} # Continue the dictionary, and replace with the real name of the emojis if needed
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            grille[i][j] = dico_emojis[grille[i][j]]
    return grille