from random import choice

random_words = ["Remolacha", "Anular", "Remolino", "Guitarra",
                "Mitologia", "Motoneta", "Saxofon", "Bromista"]
word_picked = choice(random_words).lower()
secret_word = ["_" for char in word_picked]
lifes = 6


def new_character():
    while True:
        char = input("Ingrese una letra: ").lower()
        if len(char) > 1 or char not in "abcdefghijklmnñopqrstuvwxyz":
            print(f"{char} no es una letra.")
        else:
            return char


def is_won(word):
    if "_" not in word:
        print(
            f'Has Ganado!! Adivinaste la palabra: "{word_picked}" te quedaron {lifes} vidas! ')
        return True
    return False


def start_game(word=word_picked, lifes=lifes):
    picked_chars = []
    while lifes > 0:
        print(f'Intentos restantes: {lifes}')
        char = new_character()
        for index, character in enumerate(word):
            if char == character:
                secret_word[index] = char
            else:
                pass
        picked_chars.append(char)
        print(f'Letras ya elegidas: {"-".join(picked_chars)}')
        if is_won(secret_word) is True:
            break
        print(" ".join(secret_word))
        lifes -= 1
    if lifes == 0:
        return print(f'Has perdido! La palabra era "{word_picked}" ! Intentalo nuevamente !')


start_game()
