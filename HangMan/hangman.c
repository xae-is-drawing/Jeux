#include <stdlib.h>
#include <string.h>

char *create_mask_word(char *word) {
    // Trouver la longueur du mot donné
    int length = strlen(word);
    
    // Allouer dynamiquement un tableau de caractères pour le masque
    char *mask = (char *)malloc((length + 1) * sizeof(char));

    // Remplir le tableau avec des caractères '-'
    for (int i = 0; i < length; i++) {
        mask[i] = '-';
    }

    // Ajouter le caractère de fin de chaîne
    mask[length] = '\0';

    return mask; // Retourner le tableau de caractères masqué
}

void append_letter(char letter, char *played) {
    // Trouver la longueur actuelle de la chaîne
    int length = strlen(played);

    // Ajouter le caractère à la fin de la chaîne
    played[length] = letter;

    // Ajouter le caractère de fin de chaîne '\0'
    played[length + 1] = '\0';
}

int check_letter(char letter, char * word) {
    int found = 0;
    int i = 0;
    // Parcourir la chaîne
    while (word[i] != '\0') {
        if (word[i] == letter) {
            found = 1;
            break;
        }
        i++;
    }
    return found;
}

int reveal_letter(char letter, char *word, char *mask) {
    int count = 0;
    int i = 0;
    while (word[i] != '\0') {
        if (word[i] == letter && mask[i] == '-') {
            mask[i] = letter;
            count++;
        }
        i++;
    }
    return count;
}

int found_word(char *word, char *mask) {
    int result = strcmp(word, mask);
    return !result;
}
