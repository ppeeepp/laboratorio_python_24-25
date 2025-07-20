import random
import numpy as np

class Game:
    """
    Classe contenente le meccaniche base del gioco e la sua logica.
    """
    def __init__(self):
        """
        Inizializza la partita.
        Viene eseguita un'assegnazione casuale dei montepremi ai pacchi numerati, mappati in un dizionario.
        Viene creato un set di pacchi rimanenti.
        Vengono create delle liste che conterranno i pacchi aperti e uno storico dei premi già usciti.
        """
        self.prizes = [0, 1, 5, 10, 20, 50, 100, 200, 500,
                       5000, 10000, 20000, 30000, 50000, 75000, 100000, 200000, 300000]
        random.shuffle(self.prizes)
        self.boxes = {i+1: prize for i, prize in enumerate(self.prizes)}
        self.remaining = set(self.boxes.keys())
        self.opened = []
        self.history = []
        self.player_box = None

    def choose(self, box):
        """
        Definisce l'azione di scegliere un pacco.
        """
        try:
            self.player_box = box
            self.remaining.remove(box)
        except ValueError:
            print('Scelta non valida, il pacco non è selezionabile')

    def open_box(self, box):
        """
        Definisce l'azione di apertura di un pacco, tornandone il valore.
        """
        value = 0
        try:
            value = self.boxes[box]
            self.remaining.remove(box)
            self.opened.append(box)
        except ValueError:
            print('Scelta non valida, il pacco non è selezionabile')
        return value

    def get_remaining(self):
        """
        Restituisce la lista dei montepremi ancora rimasti, riordinata.
        Verrà poi stampata dopo ogni tiro durante il gioco o utilizzata per aggiornare lo storico dei valori medi.
        """
        return sorted([self.boxes[i] for i in self.remaining])

    def update_history(self):
        """
        Aggiorna lo storico dei valori medi durante le fasi di gioco.
        Servirà per la creazione di un grafico che rappresenterà l'andamento della partita.
        """
        return self.history.append(np.mean(self.get_remaining()))

    def is_over(self):
        return len(self.remaining) == 0
