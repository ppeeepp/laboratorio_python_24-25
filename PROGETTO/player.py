from doctor import Doctor

class Player:
    """
    Classe che rappresenta il giocatore, ne descrive le caratteristiche e ne definisce le azioni nella partita
    """
    def __init__(self):
        self.box = None
        self.accepted_offer = False
        self.final_gain = None

    def choose(self, available):
        while True:
            try:
                box = int(input(f'Seleziona il tuo pacco tra i seguenti:\n{sorted(available)}\n'))
                if box in available:
                    self.box = box
                    return box
                else:
                    print('Pacco non disponibile, selezionane un altro')
            except ValueError:
                print('Inserisci un numero valido (da 1 a 20)')

    def decide(self, propose, amount=None, remaining=None):
        """
        Definisce la decisione presa dal giocatore in risposta all'offerta del dottore.
        """
        if propose == 'offer':
            decision = input(f'Il dottore ti offre: {amount} €.\nAccetti? (s/n) o (1/2)\n').strip().lower()
            if decision.startswith('s') or decision == '1':
                self.accepted_offer = True
                return self.accepted_offer
            elif decision.startswith('n') or decision == '2':
                return None
            else:
                print('Input non valido.')
                self.decide(propose, amount, remaining)
        if propose == 'swap':
            decision = input(Doctor.propose_swap()).strip().lower()
            if decision.startswith('s') or decision == '1':
                while True:
                    try:
                        choice = int(input(f'Scegli un pacco:\n{sorted(remaining)}\n'))
                        if choice in remaining:
                            return choice
                        else:
                            print('Pacco non disponibile.')
                    except ValueError:
                        print('Input non valido.')
            elif decision.startswith('n') or decision == '2':
                print('Hai rifiutato lo scambio.')
                return None
            else:
                print('Input non valido.')
                self.decide(propose, amount, remaining)


