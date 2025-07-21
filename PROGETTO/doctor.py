import numpy as np

class Doctor:
    """
    Classe che rappresenta il Dottore e ne definisce la logica
    Essendo il Dottore un'entità unica nel gioco, non ho bisogno di istanziare oggetti di tipo Doctor per eseguire azioni
    -> i metodi di questa classe sono tutti statici
    """
    @staticmethod
    def make_offer(remaining, player_box, recent):
        """
        Definisce l'azione del dottore di fare un'offerta al concorrente.
        La base considerata è la metà della media dei pacchi rimanenti,
        variabile in base a: contenuto del pacco del concorrente, deviazione standard e andamento degli ultimi tiri.
        Ritorna un'offerta pari a un multiplo di 500.
        """
        medium_value = np.mean(remaining)
        offer = medium_value/2
        # prima considerazione: il contenuto del pacco del concorrente è > valor medio?
        if player_box > medium_value:
            offer *= 1.05
        else:
            offer *= 0.95
        # seconda considerazione: com'è andato il giocatore negli ultimi tiri?
        good = False
        for value in recent:
            if value > medium_value:
                good = True
        if good:
            offer *= 1.1
        else:
            offer *= 0.9
        # terza considerazione: quanto è la deviazione standard tra i pacchi? -> più è alto il fattore di rischio, più può alzarsi l'offerta
        std = np.std(remaining)
        if std/medium_value > 0:
            offer *= (1 + std/medium_value)
        # OFFERTA FINALE - arrotonda l'offerta al multiplo di 500 più vicino
        if offer < 1000:
            return int(round(offer/250)*250)
        elif offer < 10000:
            return int(round(offer/500) * 500)
        else:
            return int(round(offer/1000) * 1000)

    @staticmethod
    def propose_swap():
        """
        Propone al concorrente di scambiare il suo pacco con un pacco a scelta tra i rimanenti.
        """
        return 'Il dottore propone di scambiare il tuo pacco.\nAccetti lo scambio? (S/N)\n'

    @staticmethod
    def get_turn_count(player_box, remaining):
        """
        In base ai pacchi rimanenti e al pacco del concorrente, il Dottore decide quanti tiri far effettuare al giocatore.
        """
        std = np.std(remaining)
        mean = np.mean(remaining)
        ratio = std/mean if mean > 0 else 0
        shots = 0
        if ratio < 0.5:
            shots = 1
        elif 0.5 < ratio < 1.0:
            shots = 2
        elif 1.0 < ratio > 1.5:
            shots = 3
        elif 1.5 < ratio < 1.7:
            shots = 4
        elif 1.7 < ratio < 2.0:
            shots = 5
        else:
            shots = 6
        if player_box < mean:
            shots += 1
        max_shots_allowed = len(remaining) - 2
        shots = min(shots, max_shots_allowed)
        return shots

