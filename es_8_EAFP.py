# Scrivete un programma per “il gioco dell’impiccato” in cui:
    # leggete una lista di parole da un file JSON
    # scegliete una parola a caso con cui giocare dalla lista letta, tramite random
    # chiedete continuamente all’utente di inserire una lettera o di indovinare la parola, fino al termine del gioco in cui si esauriscono i tentativi o si indovina la parola
# La rappresentazione grafica del gioco è libera, così come il numero dei “tentativi” disponibili.
# 1- Scrivete il programma con un approccio totalmente LBYL
# 2- RI-scrivete il programma con un approccio totalmente EAFP

# VERSIONE EAFP
import json
import random
# leggete una lista di parole da un file JSON
def load(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, TypeError) as e:
        print(f'Errore nel caricamento del file: {e}')
        return []

def main():
    words = load('Lezioni/words.json')
    if not words:
        return
    # scegliete una parola a caso con cui giocare dalla lista letta, tramite random
    try:
        secret_word = random.choice(words).lower()
    except (IndexError, AttributeError):
        print('Errore: lista parole vuota o invalida.')
        return
    guessed = set()
    attempts = 6        # il disegno dell'omino ha 6 'tratti'
    hidden_word = ['_' if c.isalpha() else c for c in secret_word]

    print('--- IMPICCATO ---')
    # chiedete continuamente all’utente di inserire una lettera o di indovinare la parola, fino al termine del gioco in cui si esauriscono i tentativi o si indovina la parola
    while attempts > 0 and '_' in hidden_word:
        print(f'Parola: {' '.join(hidden_word)}')
        print(f'Tentativi rimasti: {attempts}')
        # controllo input
        try:
            letter = input('Inserisci una lettera o prova a indovinare la parola: ').lower().strip()
        except Exception as e:
            print(f'Errore durante l\'input: {e}')
            continue
        # controllo se lettera inserita è alfabetica
        try:
            if len(letter) == 1:
                if letter in guessed:
                    print('Lettera già usata.')
                    continue
                guessed.add(letter)
                if letter in secret_word:
                    hidden_word = [c if c in guessed else '_' for c in secret_word]
                else:
                    attempts -= 1
                    print('Lettera sbagliata!')
            elif letter == secret_word:
                hidden_word = list(secret_word)
            else:
                attempts -= 1
                print('Parola sbagliata!')
        except (ValueError, Exception):
            print(f'Errore nell\'elaborazione dell\'input: {Exception}')
            continue
    if '_' not in hidden_word:
        print(f'INDOVINATO! {secret_word}')
    else:
        print(f'HAI PERSO - La parola era: {secret_word}')

if __name__ == '__main__':
    main()
