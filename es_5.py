import random
import time

# Dalla lezione 7: funzioni stessa_diagonale() e incrocia_colonne()
def same_diagonal(x0, y0, x1, y1):
    return abs(x1-x0)-abs(y1-y0)

def cross_columns(pos, col):
    for c in range(col):
        if same_diagonal(c, pos[c], col, pos[col]):
            return True
    return False

def is_valid(pos):
    """
    controlla se una disposizione di regine è valida -> non ci sono coppie sulla stessa diagonale dappertutto
    :param pos: lista di interi -> l'indice è la riga, il valore (pos[i]) la colonna
    :return: True se la disposizione è valida, False altrimenti
    """
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            if abs(i - j) == abs(pos[i] - pos[j]):
                return False  # stessa diagonale
    return True
# 1) Trovate 10 soluzioni per il gioco delle regine con il metodo delle permutazioni:
#     quanto è il tempo medio necessario a trovare una soluzione?
#     2) Contate quanti tentativi fa il programma per trovare ogni soluzione del problema 8 regine
# ho unito questi due punti in una funzione sola
def get_10_med_time():
    """
    Inizializza una lista di soluzioni, il numero di tentativi e memorizza il tempo di partenza.
    Appena trova una soluzione valida, la salva finchè la lista non si riempie
    Alla fine delle iterazioni, salva il tempo finale e, facendo la differenza con quello iniziale, calcola la media.
    """
    random_gen = random.Random()
    solutions = []
    attempts = 0
    start = time.time()
    while len(solutions)<10:
        list_of_solutions = list(range(8))
        random_gen.shuffle(list_of_solutions)
        attempts += 1
        if is_valid(list_of_solutions):
            print(f'Soluzione trovata: {list_of_solutions}\nNumero tentativi: {attempts}')
            solutions.append(list_of_solutions.copy())
            attempts = 0
    end = time.time()
    total_time = end - start
    med_time = total_time/10
    print(f'Tempo medio per trovare una soluzione: {med_time:.3f}s')

# 3) Alcune soluzioni possono essere ripetute: fate in modo che le soluzioni siano “uniche”
def get_unique_solutions():
    """
    Salva le soluzioni in un set per evitare duplicati.
    La lista di soluzioni viene poi trasformata in tupla per poter essere aggiunta al set,
    perchè altrimenti sarebbe mutabile, quindi non hashabile.
    """
    random_gen = random.Random()
    unique_solutions = set()                    # set di soluzioni, per non avere duplicati
    attempts = 0
    total_attempts = 0
    n_solutions = 10
    while len(unique_solutions) < n_solutions:
        list_of_solutions = list(range(8))
        random_gen.shuffle(list_of_solutions)
        attempts += 1
        if is_valid(list_of_solutions):
            tuple_of_solutions = tuple(list_of_solutions)   # converto la lista in tupla per poterla aggiungere al set
            if tuple_of_solutions not in unique_solutions:
                unique_solutions.add(tuple_of_solutions)
                print(f'Soluzione {len(unique_solutions)} trovata: {list_of_solutions}\nNumero tentativi: {attempts}')
                total_attempts += attempts
                attempts = 0
    return unique_solutions

# 4) Se ci sono soluzioni ripetute, contate quante volte ogni soluzione è ripetuta
def count_repetitions():
    """
    Genera migliaia di soluzioni valide, e verifica quante volte vengono ripetute
    """
    max_attempts = 10000
    random_gen = random.Random()
    repetitions = {}
    for attempt in range(max_attempts):
        list_of_solutions = list(range(8))
        random_gen.shuffle(list_of_solutions)
        if is_valid(list_of_solutions):
            tuple_of_solutions = tuple(list_of_solutions)
            if tuple_of_solutions in repetitions:
                repetitions[tuple_of_solutions] += 1
            else:
                repetitions[tuple_of_solutions] = 1
    return repetitions

# 5) Generalizzate il programma per risolvere una scacchiera di qualunque dimensione NxN
# riscrivo la funzione get_unique_solutions() per trovare soluzioni uniche per una scacchiera NxN
# stavolta n_solutions è messo come parametro di ingresso, per scegliere quante soluzioni si vogliono trovare
def get_unique_solutions_nxn(n, n_solutions):
    """
       Trova soluzioni uniche per il problema delle N regine su una scacchiera NxN.
       Viene generata una configurazione casuale di N regine (una per riga) e si verifica se è valida.
       Se la soluzione è valida viene salvata in un set
       che verrà riempito fino a trovare il numero richiesto di soluzioni uniche.
       :param n: dimensione della scacchiera
       :param n_solutions: numero di soluzioni uniche da trovare
       :return: set di tuple - ogni tupla rappresenta una soluzione valida
       :raises: stringa di errore in caso di parametri non validi o eccezioni
       """
    try:                                                            # controllo dei parametri di ingresso
        if n > 0 and n_solutions > 0:
            random_gen = random.Random()
            unique_solutions = set()                                # set di soluzioni, per non avere duplicati
            attempts = 0
            total_attempts = 0
            while len(unique_solutions) < n_solutions:
                list_of_solutions = list(range(n))
                random_gen.shuffle(list_of_solutions)
                attempts += 1
                if is_valid(list_of_solutions):
                    tuple_of_solutions = tuple(list_of_solutions)   # converto la lista in tupla per poterla aggiungere al set
                    if tuple_of_solutions not in unique_solutions:
                        unique_solutions.add(tuple_of_solutions)
                        print(f'Soluzione {len(unique_solutions)} trovata: {list_of_solutions}\nNumero tentativi: {attempts}')
                        total_attempts += attempts
                        attempts = 0
            return unique_solutions
    except Exception as e:
        return f'{e}: Parametro/i non valido/i!'

# 6) Trovate quale è la scacchiera con lato N più grande possibile per cui si riesce a trovare 1 soluzione in meno di 30s
def find_max_n():
    n = 8
    random_gen = random.Random()
    while True:
        attempts = 0
        start = time.time()
        found = False
        while time.time() - start < 30:
            list_of_solutions = list(range(n))
            random_gen.shuffle(list_of_solutions)
            attempts += 1
            if is_valid(list_of_solutions):
                print(f'Lato: {n}\nSoluzione trovata: {list_of_solutions}\nTentativi: {attempts}\nTempo impiegato: {(time.time() - start):.3f}s')
                found = True
                break
        if not found:
            return f'Max N: {n-1}'
        else:
            n += 1

# 7) Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi.
#    Scrivete delle funzioni che, una volta trovata una soluzione alla scacchiera, costruiscano le 4 soluzioni simmetriche per rotazione.
#    Trovate 10 soluzioni uniche e le rispettive simmetriche per una scacchiera 8x8
# ROTAZIONI
def rotate_90(solution):
    n = len(solution)
    rotated = [0]*n
    for row, col in enumerate(solution):
        # dopo rotazione di 90 gradi la regina in (row, col) va in (c, n-1-r)
        rotated[col] = n-1-row
    return rotated
def get_all_rotations(solution):
    rotations = [solution]
    current = solution
    for rot in range(3):
        current = rotate_90(current)
        rotations.append(current)
    return rotations
# TROVA SOLUZIONI UNICHE + SIMMETRICHE
# estendo la funzione get_unique_solutions_nxn()
def get_unique_solutions_nxn_and_simmetric(n, n_solutions):
    """
    L'obiettivo è quello di trovare [n_solutions] soluzioni valide.
    Queste soluzioni devono essere simmetriche -> quelle che si differenziano
    perchè sono rotazioni di altre soluzioni non devono essere conteggiate.
    Per farlo, una volta trovata una soluzione, trovo tutte le sue rotazioni
    e verifico che non vengano aggiunte alla lista delle soluzioni.
    :param n: lato scacchiera
    :param n_solutions: numero soluzioni che voglio trovare
    :return: lista contenente le soluzioni uniche trovate
    """
    try:                                                            # controllo dei parametri di ingresso
        if n > 0 and n_solutions > 0:
            random_gen = random.Random()
            unique_solutions = []
            rotations = set()                                       # set di ROTAZIONI
            attempts = 0
            total_attempts = 0

            while len(unique_solutions) < n_solutions:
                list_of_solutions = list(range(n))
                random_gen.shuffle(list_of_solutions)
                attempts += 1

                if is_valid(list_of_solutions):
                    rotated_solutions = get_all_rotations(list_of_solutions)        # ottengo tutte le rotazioni della soluzione trovata
                    tuples_of_solutions = [tuple(r) for r in rotated_solutions]     # converto la lista in tuple per poterla aggiungere al set
                    already_seen = False                                            # controllo che una soluzione non sia già presente in rotations
                    for tup in tuples_of_solutions:
                        if tup in rotations:
                            already_seen = True
                            print(f'Soluzione già presente - numero tentativi: {attempts}')
                            break
                    if not already_seen:
                        unique_solutions.append(list_of_solutions.copy())
                        rotations.update(tuples_of_solutions)
                        print(f'Soluzione {len(unique_solutions)} trovata dopo {attempts} tentativi: {list_of_solutions}')
                        attempts = 0
            return unique_solutions
    except Exception as e:
        return f'{e}: Parametro/i non valido/i!'

if __name__ == '__main__':
    #get_10_med_time()
    #print(get_unique_solutions())
    #print(count_repetitions())
    #print(get_unique_solutions_nxn(15, 10))
    #print(find_max_n())
    #print(get_unique_solutions_nxn_and_simmetric(8, 10))
    print()

