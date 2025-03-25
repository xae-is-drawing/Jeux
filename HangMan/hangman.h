#ifndef HANGMAN_P1_HANGMAN_H
#define HANGMAN_P1_HANGMAN_H

char * get_word();

char * create_mask_word(char * word);

void append_letter(char letter, char * played);

int check_letter(char letter, char * word);

int reveal_letter(char letter, char * word, char * mask);

int found_word(char * word, char * mask);


#endif //HANGMAN_P1_HANGMAN_H