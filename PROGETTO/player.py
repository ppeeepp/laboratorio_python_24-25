
class Player:
    """
    Classe che rappresenta il giocatore, ne descrive le caratteristiche e ne definisce le azioni nella partita
    """
    def __init__(self):
        self.box = None
        self.accepted_offer = None
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
                print('Inserisci un numero valido  (da 1 a 20)')

    def decide(self, propose, amount=None, remaining=None):
        if propose == 'offer':
            decision = input(f'Il dottore ti offre: {amount} €.\nAccetti? (s/n)\n').strip().lower()
            self.accepted_offer = decision.startswith('s')
            return self.accepted_offer
        if propose == 'swap':
            decision = input('Il dottore ti offre di scambiare il tuo pacco con uno dei rimanenti.\nAccetti? (s/n)\n').strip().lower()
            if decision.startswith('s'):
                while True:
                    try:
                        choice = int(input(f'Scegli un pacco:\n{sorted(remaining)}\n'))
                        if choice in remaining:
                            return choice
                        else:
                            print('Pacco non disponibile.')
                    except ValueError:
                        print('Input non valido.')
            else:
                print('Hai rifiutato lo scambio.')
                return None


