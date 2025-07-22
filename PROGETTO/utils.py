from doctor import Doctor
import logging
from game import Game
import matplotlib.pyplot as plt

"""
File con tutte le funzionalità utili che vengono chiamate nel main
"""
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def play_turn(game, player, n_turn, turns, recent_values):
    """
    Funzione che rappresenta lo svolgimento di un turno.
    L'utente può scegliere tra due azioni:
    - aprire un pacco
    - mostrare a schermo lo storico delle offerte del dottore, se presenti, e il loro stato (accettata/rifiutata).
    Ritorna il numero di turno successivo.
    """
    for t in range(turns):
        if game.is_over():
            break

        print(f'-------\nTURNO {n_turn}\n-------')
        while len(game.remaining) > 2:
            print(f'Pacchi rimasti: {sorted(game.remaining)}')
            print(f'Montepremi rimasti: {sorted(game.get_remaining())}')
            action = input(
                'Cosa vuoi fare?\n[1] Apri un pacco\n[2] Vedi storico offerte\n').strip()
            if action == '1':
                try:
                    box = int(input(f'Scegli un pacco da aprire.\n'))
                    if box in game.remaining:
                        value = game.open_box(box)
                        recent_values.append(value)
                        print(f'Il pacco n. {box} conteneva: {value} €')
                        game.update_box_history()
                        game.player_box_history.append(game.boxes[player.box])
                        logging.info(f'Turno {n_turn} - Valore pacco {box}: {value} EUR')
                        break
                    else:
                        print('Pacco non disponibile')
                        continue
                except (ValueError, Exception):
                    print('Inserisci un numero valido.')
            elif action == '2':
                if not game.offer_history:
                    print('Nessuna offerta ricevuta finora.')
                else:
                    print('Storico offerte:')
                    for offer in game.offer_history:
                        description = f'{offer['type'].upper()} - {'EUR'if type(offer['value'])==int else None} {offer['value'] if type(offer['value'])==int else 'CAMBIO'} - {'ACCETTATA' if offer['accepted'] else 'RIFIUTATA'}'
                        print(f'Turno {offer['turn']}: {description}')
            else:
                print('Scelta non valida. Seleziona [1] o [2]')
        n_turn += 1
    return n_turn, game.boxes[player.box]

def handle_offer(game, player, player_box, recent_values, cur_turn, random_gen):
    """
    Gestisce la proposta del Dottore nel main.
    Ritorna una tupla: (True, 0) se l'offerta è stata accettata -> il gioco termina, altrimenti ritorna (False, turn_count).
    """
    remaining = game.get_remaining()
    turn_count = Doctor.get_turn_count(player_box, remaining)
    print(f'PROPOSTA - Il Dottore ti fa aprire {turn_count} pacchi se non accetti la seguente proposta:')
    offer_type = random_gen.choice(['offer']*3 + ['swap'])  # nei test notavo che il dottore offriva troppe volte il cambio.
                                                            # Per renderlo più realistico ho aumentato le probabilità dell'offerta economica: 3/4 offerta, 1/4 scambio.
    if offer_type == 'offer':
        offer = Doctor.make_offer(remaining, game.boxes[player.box], cur_turn, recent_values)
        accepted = player.decide(propose='offer', amount=offer)
        game.update_offer_history(turn=cur_turn-1, offer=offer, status=accepted)    # cur_turn-1 perchè è stato incrementato da in play_turn
        if accepted:
            print(f'Hai accettato l\'offerta di {offer} €!')
            player.final_gain = offer
            return True, 0  # fine del gioco
        elif not accepted:
            print('Hai rifiutato l\'offerta')
            return False, turn_count
    else:
        accepted_swap = player.decide(propose='swap', remaining=game.remaining)
        game.update_offer_history(turn=cur_turn-1, offer='swap', status=bool(accepted_swap))
        if accepted_swap:
            game.remaining.add(player.box)  # rimette il vecchio pacco nel set
            game.player_box_history.append(game.boxes[game.player_box])
            game.choose(accepted_swap)
            player.box = accepted_swap
            print(f'Hai scambiato il tuo pacco con il pacco n. {accepted_swap}')
    return False, turn_count

def get_game_plot(box_values, mean, offers):
    """
    Fornisce un grafico dell'andamento della partita.
    i 3 dati mostrati saranno:
    - il valore del pacco del concorrente       <- input: box_values = lista dei valori del pacco del concorrente per turno
    - l'andamento del valor medio dei pacchi    <- input: mean
    - l'andamento delle offerte del dottore     <- input: offers
    L'asse x rappresenta l'andamento temporale della partita: numero di tiri, dal primo al 19esimo.
    """
    min_len = min(len(mean), len(box_values))               # per evitare incongruenze negli input, trovo il minimo dei punti comuni a tutti i grafici
                                                            # quando verrà chiamato, verrà effettuato lo slicing
    n_turns = list(range(1, min_len+1))                     # preparazione dell'asse x --> min_len+1 perchè se no si ferma a 18
    offer_turns = [offer['turn'] for offer in offers]       # estrazione dei dati delle offerte
    offer_values = [offer['value'] for offer in offers]
    fig, graph = plt.subplots(nrows=1, ncols=1)
    graph.plot(n_turns, box_values[:min_len], label='Valore pacco concorrente', linestyle='--', color='orange')
    graph.plot(n_turns, mean[:min_len], label='Valor medio dei pacchi', color='green')
    graph.plot(offer_turns, offer_values, label='Offerte del dottore', linestyle='--', color='blue', marker='+')
    graph.set_xlabel('Turni')
    graph.set_ylabel('EUR')
    graph.legend()
    graph.grid(True)
    plt.show()

