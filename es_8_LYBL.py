# Scrivete un programma per “il gioco dell’impiccato” in cui:
    # leggete una lista di parole da un file JSON
    # scegliete una parola a caso con cui giocare dalla lista letta, tramite random
    # chiedete continuamente all’utente di inserire una lettera o di indovinare la parola, fino al termine del gioco in cui si esauriscono i tentativi o si indovina la parola
# La rappresentazione grafica del gioco è libera, così come il numero dei “tentativi” disponibili.
# 1- Scrivete il programma con un approccio totalmente LBYL
# 2- RI-scrivete il programma con un approccio totalmente EAFP

# VERSIONE LBYL
import json
import random
# leggete una lista di parole da un file JSON
def load(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        if content:
            words = json.loads(content)
            if isinstance(words, list) and all(isinstance(p, str) for p in words):
                return words

def main():
    words = load('Lezioni/words.json')
    if not words:
        return
    # scegliete una parola a caso con cui giocare dalla lista letta, tramite random
    secret_word = random.choice(words).lower()
    guessed = set()
    attempts = 6        # il disegno dell'omino ha 6 'tratti'
    hidden_word = ['_' if char.isalpha() else char for char in secret_word]

    print('--- IMPICCATO ---')
    # chiedete continuamente all’utente di inserire una lettera o di indovinare la parola, fino al termine del gioco in cui si esauriscono i tentativi o si indovina la parola
    while attempts > 0 and '_' in hidden_word:
        print(f'\nParola: {' '.join(hidden_word)}')
        print(f'Tentativi rimasti: {attempts}')
        letter = input('Inserisci una lettera o prova a indovinare la parola: ').lower().strip()
        # controllo input
        if not letter:
            print('Input vuoto.')
            continue
        # controllo se lettera inserita è alfabetica
        if letter.isalpha():
            # controllo lettera singola
            if len(letter) == 1:
                # controllo se lettera è già indovinata
                if letter in guessed:
                    print('Hai già inserito questa lettera.')
                # lettera indovinata
                elif letter in secret_word:
                    guessed.add(letter)
                    hidden_word = [c if c in guessed else "_" for c in secret_word]
                # lettera sbagliata
                else:
                    guessed.add(letter)
                    attempts -= 1
                    print('Lettera sbagliata!')
            # controllo se ho provato a indovinare la parola
            elif len(letter) == len(secret_word):
                if letter == secret_word:
                    hidden_word = list(secret_word)
                else:
                    attempts -= 1
                    print('Parola sbagliata!')
            else:
                print('Lunghezza non valida')
        else:
            print('Errore - inserire solo lettere')
    # controllo se non ci sono più spazi vuoti
    if '_' not in hidden_word:
        print(f'INDOVINATO!')
    else:
        print(f'HAI PERSO - La parola era: {secret_word}')

if __name__ == '__main__':
    main()
