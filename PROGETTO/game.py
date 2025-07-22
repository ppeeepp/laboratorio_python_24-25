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
        Vengono create delle liste che conterranno: i pacchi aperti, uno storico dei premi già usciti e uno storico di offerte del dottore.
        """
        self.prizes = [0, 1, 5, 10, 20, 50, 75, 100, 200, 500,
                       5000, 10000, 15000, 20000, 30000, 50000, 75000, 100000, 200000, 300000]
        random.shuffle(self.prizes)
        self.boxes = {i+1: prize for i, prize in enumerate(self.prizes)}
        self.remaining = set(self.boxes.keys())
        self.opened = []
        self.box_history = []
        self.offer_history = []     # sarà una lista di dizionari contenenti il tipo di offerta e il valore
        self.player_box = None

    def choose(self, box):
        """
        Definisce l'azione di scegliere un pacco.
        """
        if box not in self.remaining:
            raise ValueError('Pacco già scelto o non valido.')
        self.player_box = box
        self.remaining.remove(box)

    def open_box(self, box):
        """
        Definisce l'azione di apertura di un pacco, tornandone il valore.
        """
        value = self.boxes[box]
        self.remaining.remove(box)
        self.opened.append(box)
        return value

    def get_remaining(self):
        """
        Restituisce la lista dei montepremi ancora rimasti, riordinata.
        Verrà poi stampata dopo ogni tiro durante il gioco o utilizzata per aggiornare lo storico dei valori medi.
        """
        return sorted([self.boxes[i] for i in self.remaining])

    def update_box_history(self):
        """
        Aggiorna lo storico dei valori medi durante le fasi di gioco.
        Servirà per la creazione di un grafico che rappresenterà l'andamento della partita.
        """
        self.box_history.append(np.mean(self.get_remaining()))

    def update_offer_history(self, turn, offer, status):
        """
        Aggiorna lo storico delle offerte durante le fasi di gioco.
        Servirà per la creazione di un grafico che rappresenterà l'andamento delle offerte del dottore.
        """
        self.offer_history.append({
            'turn': turn,
            'type': 'offerta' if type(offer) == int else 'cambio',
            'value': offer,
            'accepted': status
        })

    def is_over(self):
        return len(self.remaining) == 0
