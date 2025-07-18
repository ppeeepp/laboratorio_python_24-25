testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

# 1) Contate le righe (di effettivo testo, cioè escludendo le righe vuote) che compongono l’estratto
def count_effective_rows(text):
    rows = text.strip().split('\n')
    non_empty_rows = [row for row in rows if row.strip() != '']
    return len(non_empty_rows)

# 2) Contate le parole che compongono l’estratto
def word_count(text):
    words = text.split(' ')
    return len(words)

# 3) Contate i caratteri che compongono l’estratto
def count_chars(text):
    chars = [char for char in text if char not in '\n']
    return len(chars)

# 4) Sostituite le parole day, water e about con la parola PYTHON in tutti i versi
def replace_words(text):
    words_to_be_replaced = {'day', 'water', 'about'}
    return '\n'.join(
        [
        ' '.join(
            [
            'PYTHON' + word[len(word.strip('.,:;?!')):]                 # per mantenere la punteggiatura
            if word.strip('.,:;?!').lower() in words_to_be_replaced     # seleziono la parola senza punteggiatura
            else word for word in line.split()                          # divido ogni riga in parole separate da spazio
            ])
        for line in text.split('\n')                                    # divido il testo in righe
        ])

# 5) Riscrivete il testo con tutte le parole in posizione dispari scritte in maiuscolo
def odd_words_uppercase(text):
    return '\n'.join(
        [
        ' '.join(
            [word.upper() if i%2==0
             else word for i, word in enumerate(line.split())
            ])
            for line in text.split('\n')
        ])

# 6) Riscrivete il testo, scrivendo a specchio (cioè al contrario carattere per carattere) il secondo verso di ogni strofa (‘Ad esempio, questa frase’ –> ‘esarf atseuq ,oipmese dA’)
def invert_second_line(text):
    strophes = text.strip().split('\n\n')
    inverted = []               # lista delle stringhe invertite
    for strophe in strophes:
        lines = strophe.strip().split('\n')
        lines[1] = lines[1][::-1]   # inverto la seconda riga di ogni strofa
        inverted.append('\n'.join(lines))
    return '\n\n'.join(inverted)

# 7) Trovate eventuali parole che compaiono in tutte le strofe
def word_in_every_strophe(text):
    strophes = text.strip().split('\n\n')
    sets_of_words = []      # lista di set di parole
    for strophe in strophes:
        words = {
            word.strip('.,;:?!').lower()
            for line in strophe.split('\n')
            for word in line.split()
        }
        sets_of_words.append(words)
    common = sets_of_words[0]
    if sets_of_words:
        for corrispondence in sets_of_words[1:]:
            common = common & corrispondence
    return common

# 8) Create la lista univoca di tutte le parole che compaiono nel testo e ordinatela per lunghezza delle parole e visualizzatela
def sort_by_length(text):
    words = {
        word.strip('.,;:?!').lower()
        for line in text.split('\n')
        for word in line.split()
    }
    list_of_words = list(words)
    list_of_words.sort(key=len)
    return list_of_words

# 9) Create un dizionario che mappi OGNI carattere (chiave) con la sua occorrenza nel testo (valore) e visualizzatelo
def char_frequency(text):
    return {char: text.count(char) for char in set(text)}

# 10) Create un dizionario come il precedente per le sole lettere (no caratteri speciali), ignorando maiuscole e minuscole
def letters_frequency(text):
    return {char: text.lower().count(char) for char in set(text) if char.isalpha()}

if __name__ == '__main__':
    #print(count_effective_rows(testo))
    #print(word_count(testo))
    #print(count_chars(testo))
    #print(replace_words(testo))
    #print(invert_second_line(testo))
    #print(word_in_every_strophe(testo))
    #print(sort_by_length(testo))
    #print(char_frequency(testo))
    #print(letters_frequency(testo))
    print()
