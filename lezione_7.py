# PROBLEMA 8 REGINE
# Il rompicapo (o problema) delle otto regine è un problema che consiste nel trovare il modo di posizionare otto donne (pezzo degli scacchi)
# su una scacchiera 8x8 tali che nessuna di esse possa catturarne un’altra, usando i movimenti standard della regina.
# Perciò, una soluzione dovrà prevedere che nessuna regina abbia una colonna, traversa o diagonale in comune con un’altra regina.

scacchiera = [[0,0,0,1,0,0,0,0],
              [0,0,0,0,0,0,1,0],
              [0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,1],
              [0,1,0,0,0,0,0,0],
              [0,0,0,0,1,0,0,0],
              [1,0,0,0,0,0,0,0],
              [0,0,0,0,0,1,0,0]]

# LISTA ANNIDATA
# accedere ad una riga
prima_riga = scacchiera[0]
# accedere ad una colonna (elemento della riga)
quarta_colonna = prima_riga[3]
# combinare i due passaggi
prima_riga_quarta_colonna = scacchiera[0][3]

def valid_position(scacchiera, riga, colonna):
    # NO altre regine (valore == 1= nella stessa riga
    # loop e se un'altra colonna ha una regina, stop
    for c in range(0, 8):
        if scacchiera[riga][c] == 1:
            return False
    # NO altre regine sulla stessa colonna:
    # loop se un'altra riga ha una regina nella stessa colonna, stop
    for r in range(0, 8):
        if scacchiera[r][colonna] == 1:
            return False
    # NO altre regine sulla stessa diagonale:
    # loop righe e loop colonne, se diagonale ha un'altra regina, stop
    for r in range(0, 8):
        for c in range(0, 8):
            if r + c == riga + colonna and scacchiera[r][c] == 1:
                return False
    # NO altre regine su diagonale opposta
    # loop righe e loop colonne, se diagonale ha un'altra regina, stop
    for r in range(0, 8):
        for c in range(0, 8):
            if r - c == riga - colonna and scacchiera[r][c] == 1:
                return False
    # se la funnzione non è uscita prima, allora il posto è valido
    return True

# APPROCCIO RICORSIVO
def posiziona_regina(scacchiera, riga):
    # Verifica se una posizione nell riga è valida e posiziona una regina
    if riga >= 8:
        # condizione finale
        print('Soluzione trovata')
    else :
        # caso ricorsivo
        for col in range(8):
            # per ogni colonna controllo se poszione va bene
            if valid_position(scacchiera, riga, col) :
                # se la posizione va bene, metto la regina
                scacchiera[riga][col] = 1
                # continuo con la riga successiva in modo ricorsivo
                posiziona_regina(scacchiera, riga + 1)
                scacchiera[riga][col] = 0

# APPROCCIO BRUTE FORCE - dispone 8 regine in una posizione casuale e verifica che vadano bene
# Ma… ci sono 4426165368 modi per posizionare 8 regine in 64 caselle.
# Non è pensabile provarli tutti

# Ragiono sulla struttura dati
# Gran parte della struttura dati che uso (= la lista annidata) è vuota: contiene solo zeri
# L'informazione utile per la soluzione del problema è rappresentata dalle POSIZIONI delle regine sulla scacchiera
# = dove il valore è 1
# Poiché le posizioni 'riga' e 'colonna' sono concettualmente legate,
# li possiamo identificare con un unico elemento.
# -> PUNTO: tupla = coppia di coordinate (riga, colonna) -> indica la posizione della regina sulla scacchiera
# -> POSIZIONI: lista di 8 punti in cui si trovano le regine
posizioni = [(0,3), (1,6), (2,2), (3,7), (4,1), (5,4), (6,0), (7,5)]
# poiché qualunque soluzione valida prevede che le regine non siano sulla stessa riga,
# il valore riga deve andare da 0 a 7 senza ripetizioni
# Se guardiamo meglio la lista delle posizioni, possiamo vedere che le coordinate riga di ogni punto,
# possono essere usate come indici dei valori dentro la lista.
posizioni_indici = [3, 6, 2, 7, 1, 4, 0, 5]
# => ho condensato l'informazione utile per la soluzione del problema:
# le regine NON possono condividere la stessa colonna
# --> trovare le soluzioni del problema on questa struttura dati equivale a
#     trovare le PERMUTAZIONI della lista di 8 elementi
# che soddisfano le condizioni:
# NO stessa riga -> validato per costruzione perché l'indice della lista è univoco
# NO stessa colonna -> validato per costruzione perché i valori vanno da 0 a 7 e non si ripetono
# NO stessa diagonale: UNICA CONDIZIONE DA VERIFICARE
def stessa_diagonale(x0, y0, x1, y1):
    '''
    Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    # distanza lungo y
    dy = abs(y1 - y0)
    # distanza lungo x
    dx = abs(x1 - x0)
    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy

# e va verificato per ogni elemento (indice di colonna) della lista delle possibili soluzioni
def incrocia_colonne(posizioni, col):
    '''
    Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna
      delle posizioni delle regine precedenti
    '''
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):
        # la coordinata X (la riga) è indice (c)
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True
    # nessun incrocio, la posizione va bene e NON incrocia altre colonne
    return False

# per trovare una soluzione è possibile:
# 1) Verificare tutte le permutazioni in ordine: approccio brute force puro
# 2) Costruire delle permutazioni casuali e verificare se sono corrette: approccio statistico

# Per generare una permutazione casuale della “lista soluzione”,
# possiamo usare il metodo shuffle() dell’oggetto Random del modulo random di Python:
# modulo
import random
# oggetto Random
random_generator = random.Random()
# lista da mescolare
lista_soluzione = list(range(8))
# permutazione casuale della lista soluzione
random_generator.shuffle(lista_soluzione)
# WARNING: shuffle() modifica l'oggetto su cui agisce