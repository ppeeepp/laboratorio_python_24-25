from game import Game
from player import Player
import utils
import random

def main():
    with open('logs.log', 'w'):
        pass                    # WIPE DEL FILE DI LOG
    print('BENVENUTO AD AFFARI TUOI')

    # inizializzo tutto
    game = Game()
    player = Player()
    random_generator = random.Random()
    recent_values = []
    cur_turn = 1
    offer_counter = 0

    # scelta del pacco
    player_box = player.choose(game.remaining)
    game.choose(player_box)
    player.box = player_box
    print(f'Hai scelto il pacco n. {player_box}')

    # inizio partita: il giocatore deve effettuare 6 tiri
    print('----- INIZIO PARTITA -----')
    print('Dovrai effettuare 6 tiri prima della prima offerta del dottore.')
    cur_turn, cur_box_value = utils.play_turn(game, player, cur_turn, 6, recent_values)
    # al termine del numero di tiri, il dottore fa la sua offerta
    while not game.is_over():
        offer_counter += 1
        accepted, turn_count = utils.handle_offer(game, player, player_box, recent_values, cur_turn, random_generator)
        if accepted:
            break
        cur_turn, cur_box_value = utils.play_turn(game, player, cur_turn, turn_count, recent_values)
        # finale della partita: rimangono solo il pacco del giocatore e un ultimo pacco. Il dottore fa la sua ultima offerta
        if not player.accepted_offer and len(game.remaining) == 2:
            print('----- ULTIMA OFFERTA DEL DOTTORE -----')
            offer_counter += 1
            accepted, _ = utils.handle_offer(game, player, game.boxes[player.box], recent_values, cur_turn, random_generator)
            if accepted:
                break
            break
        # fine partita
    player.final_gain = game.boxes[player.box]
    print(f'Il tuo pacco conteneva: {game.boxes[player.box]} €')
    print(f'Guadagno finale: {player.final_gain} €')
    print('A schermo verrà stampato il grafico con l\'andamento della tua partita.')
    utils.get_game_plot(box_values=game.player_box_history, mean=game.box_history, offers=game.offer_history)
    # chiede se vuoi rigiocare
    rematch = input('Vuoi giocare ancora? (s/n)\n').strip().lower()
    if rematch.startswith('s'):
        main()
    else:
        exit(0)


main()
