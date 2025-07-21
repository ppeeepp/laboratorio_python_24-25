from game import Game
from player import Player
from doctor import Doctor
import random

def play_turn(game, player, n_turn, turns, recent_values):
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
                        n_turn += 1
                        break
                    else:
                        print('Pacco già aperto o non valido.')
                except ValueError:
                    print('Inserisci un numero valido.')
            elif action == '2':
                if not game.offer_history:
                    print('Nessuna offerta ricevuta finora.')
                else:
                    print("Storico offerte:")
                    for offer in game.offer_history:
                        desc = f"{offer['type'].upper()} - {offer['value']} - {'ACCETTATA' if offer['accepted'] else 'rifiutata'}"
                        print(f"Turno {offer['turn']}: {desc}")
            else:
                print("Scelta non valida.")
    return n_turn

def handle_offer(game, player, player_box, recent_values, cur_turn, rng):
    """
    Gestisce la proposta del Dottore nel main.
    Ritorna True se l'offerta è stata accettata e il gioco termina, altrimenti ritorna False.
    """
    remaining = game.get_remaining()
    turn_count = Doctor.get_turn_count(player_box, remaining)
    print(f'PROPOSTA - Il Dottore ti fa aprire {turn_count} pacchi se non accetti la seguente proposta:')
    offer_type = rng.choice(('offer', 'swap'))
    if offer_type == 'offer':
        offer = Doctor.make_offer(remaining, game.boxes[player.box], recent_values)
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
            game.remaining.add(player.box)  # rimetti il vecchio pacco nel set
            game.choose(accepted_swap)
            player.box = accepted_swap
            print(f'Hai scambiato il tuo pacco con il pacco n. {accepted_swap}')
    return False, turn_count


def main():
    print('BENVENUTO AD AFFARI TUOI')

    game = Game()
    player = Player()
    random_generator = random.Random()

    # Scelta pacco iniziale
    player_box = player.choose(game.remaining)
    game.choose(player_box)
    player.box = player_box
    print(f'Hai scelto il pacco n. {player_box}')

    recent_values = []
    cur_turn = 1

    # 6 tiri iniziali obbligatori
    print("Prima fase: 6 tiri iniziali.")
    cur_turn = play_turn(game, player, cur_turn, 6, recent_values)


    offer_counter = 0
    while not game.is_over():
        offer_counter += 1
        accepted, turn_count = handle_offer(game, player, player_box, recent_values, cur_turn, random_generator)
        if accepted:
            break
        cur_turn = play_turn(game, player, cur_turn, turn_count, recent_values)

    if len(game.remaining) == 1:
        print('----- ULTIMA OFFERTA DEL DOTTORE -----')
        offer_counter += 1
        accepted, turn_count = handle_offer(game, player, player_box, recent_values, cur_turn, random_generator)

    # Fine partita
    if not player.final_gain:
        final_value = game.boxes[player.box]
        print(f"Il tuo pacco finale (n. {player.box}) conteneva: {final_value} €")
        player.final_gain = final_value

    print(f'Il tuo pacco conteneva: {player_box} €')
    print(f'Guadagno finale: {player.final_gain} €')


if __name__ == '__main__':
    main()
