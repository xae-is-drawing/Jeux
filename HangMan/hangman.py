from wonderwords import RandomWord

def choose_word(length: int) -> str:
    '''
    Generates a word with the length given by the user
    '''
    w = RandomWord()
    word = w.word(word_min_length=length, word_max_length=length).lower()
    return word

def create_mask_word(length: int) -> str:
    '''
    Generates a string where the user will guess the word
    '''
    return '-' * length

def number_of_occurrences(letter: str, word: str) -> int:
    '''
    Returns the number of occurrences of letter in word
    '''
    return sum(1 for l in word if letter == l)

def reveal_letter(letter: str, word: str, mask: str) -> str:
    '''
    Replaces the hyphen with the letter
    Returns the modified mask string
    '''
    updated_mask = ""  # Start with an empty string
    for i in range(len(word)):
        if word[i] == letter:
            updated_mask += letter  # Add the guessed letter
        else:
            updated_mask += mask[i]  # Keep the existing character (hyphen or previously revealed letter)
    return updated_mask

def found_word(word: str, mask: str) -> bool:
    '''
    Check if the user guessed the word
    '''
    return word == mask

def get_positive_integer(prompt: str) -> int:
    '''
    Repeatedly prompts the user for a positive integer
    '''
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value > 1:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def hangman_game():
    '''
    Allows the user to play the hangman game (guess a word)
    '''
    length = get_positive_integer("How long should the word be? (Must be above 1.) ")
    word_to_guess = choose_word(length)
    guess = create_mask_word(length)
    attempts = get_positive_integer("How many guesses do you want to have? ")
    letters_to_try = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    while attempts > 0 and not found_word(word_to_guess, guess):
        print(guess)
        print(f"Number of attempt(s) left: {attempts}.")
        print("Letters you can try: ")
        for l in letters_to_try:
            print(f"{l} ", end="")
        print("")
        guessed_letter = input("Enter a letter: ").lower()
        if len(guessed_letter) != 1 or guessed_letter not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a single valid letter.")
            #continue
        if guessed_letter.upper() in letters_to_try:
            if guessed_letter in word_to_guess:
                guess = reveal_letter(guessed_letter, word_to_guess, guess)
                print(f"Well done! {guessed_letter.upper()} is present in the word.")
            else:
                attempts -= 1
                print("Letter incorrect.")
            letters_to_try.remove(guessed_letter.upper())
        else:
            print("You have already tried this letter.")

    if found_word(word_to_guess, guess):
        print(f"GG! You've found the word: {word_to_guess.upper()}!")
    else:
        print(f"Game over! The word was: {word_to_guess.upper()}.")
