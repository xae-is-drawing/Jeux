#include <stdio.h>
#include "hangman.h"

// juste un exemple dans le main
int main()
{
    char *word = get_word(); // Le mot à découvrir (à définir dans get_word)
    char *mask = create_mask_word(word); // Création du masque
    int attempts = 8; // Nombre d'essais autorisés
    char guessed_letter; // Lettre proposée par l'utilisateur
    int letters_found = 0; // Nombre de lettres découvertes

    printf("Bienvenue dans le jeu du pendu !\n");
    printf("Mot à découvrir : %s\n", mask);

    while (attempts > 0 && !found_word(word, mask)) {
        printf("\nEssais restants : %d\n", attempts);
        printf("Proposez une lettre : ");
        scanf(" %c", &guessed_letter);

        if (check_letter(guessed_letter, word)) {
            int count = reveal_letter(guessed_letter, word, mask);
            letters_found += count;
            printf("Bonne lettre ! %d lettre(s) trouvée(s).\n", count);
        } else {
            attempts--;
            printf("Lettre incorrecte. Essais restants : %d\n", attempts);
        }

        printf("Mot actuel : %s\n", mask);
    }

    if (found_word(word, mask)) {
        printf("\nFélicitations ! Vous avez découvert le mot : %s\n", word);
    } else {
        printf("\nDommage ! Vous avez perdu. Le mot était : %s\n", word);
    }

    free(word); // Libération de la mémoire dynamique
    free(mask);
    return 0;
}