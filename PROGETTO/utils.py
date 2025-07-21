from doctor import Doctor
import logging
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
        while True:
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
                        logging.info(f'Turno {n_turn} - Valore pacco {box}: {value} EUR')
                        n_turn += 1
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
                        description = f'{offer['type'].upper()} - {offer['value']} - {'ACCETTATA' if offer['accepted'] else 'RIFIUTATA'}'
                        print(f'Turno {offer['turn']}: {description}')
            else:
                print('Scelta non valida. Seleziona [1] o [2]')
    return n_turn

def handle_offer(game, player, player_box, recent_values, cur_turn, random_gen):
    """
    Gestisce la proposta del Dottore nel main.
    Ritorna una tupla: (True, 0) se l'offerta è stata accettata -> il gioco termina, altrimenti ritorna (False, turn_count).
    """
    remaining = game.get_remaining()
    turn_count = Doctor.get_turn_count(player_box, remaining)
    print(f'PROPOSTA - Il Dottore ti fa aprire {turn_count} pacchi se non accetti la seguente proposta:')
    offer_type = random_gen.choice(['offer']*2 + ['swap'])  # nei test notavo che il dottore offriva troppe volte il cambio.
                                                            # Per renderlo più realistico ho aumentato le probabilità dell'offerta economica: 2/3 offerta, 1/3 scambio.
    if offer_type == 'offer':
        offer = Doctor.make_offer(remaining, game.boxes[player.box], cur_turn, recent_values)
        accepted = player.decide(propose='offer', amount=offer)
        game.update_offer_history(turn=cur_turn, offer=offer, status=accepted)
        if accepted:
            print(f'Hai accettato l\'offerta di {offer} €!')
            player.final_gain = offer
            return True, 0  # fine del gioco
    else:
        accepted_swap = player.decide(propose='swap', remaining=game.remaining)
        game.update_offer_history(turn=cur_turn, offer='swap', status=bool(accepted_swap))
        if accepted_swap:
            game.remaining.add(player.box)  # rimette il vecchio pacco nel set
            game.choose(accepted_swap)
            player.box = accepted_swap
            print(f'Hai scambiato il tuo pacco con il pacco n. {accepted_swap}')
    return False, turn_count