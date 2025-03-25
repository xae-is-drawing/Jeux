'''
JEU DE BASE
''' 

def generate_grid():
    grille = [[0 for j in range(4)] for i in range(4)]
    return grille

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
    mov = ['u', 'r', 'l', 'd'] #up, right, left, down
    print("Press U for UP, D for DOWN, R for RIGHT and L for LEFT.")
    key_pressed = input().lower()
    while key_pressed not in mov:
        print("Invalid key. It must be U or D or R or L.")
        key_pressed = input().lower()
    if key_pressed == 'r':
        direction = "right"
    elif key_pressed == 'l':
        direction = "left"
    elif key_pressed == 'u':
        direction = "up"
    else:
        direction = "down"
    return direction 

def add_right():
    pass

def add_left():
    pass

def add_up():
    pass

def add_down():
    pass

def add_numbers(grille):
    # IN : grille ()
    # OUT : grille ()
    # Modifies the inputed grille so that it actualises
    way = wanted_direction()
    if way == "right":
        add_right()
    elif way == "left":
        add_left()
    elif way == "up":
        add_up()
    else:
        add_down()

'''
DISCORD VERSION
''' 

def discord_emojis(grille):
    dico_emojis = {2:"number_2", 4:"number_4", 8:"number_8", 16:"number_16", 32:"number_32", 64:"number_64", 128:"number_128", 256:"number_256"} # Continue the dictionary, and replace with the real name of the emojis if needed
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            grille[i][j] = dico_emojis[grille[i][j]]
    return grille