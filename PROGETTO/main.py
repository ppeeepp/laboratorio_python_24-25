from game import Game
from player import Player
import utils
import random

def main():
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
    cur_turn = utils.play_turn(game, player, cur_turn, 6, recent_values)
    # al termine del numero di tiri, il dottore fa la sua offerta
    while not game.is_over():
        offer_counter += 1
        accepted, turn_count = utils.handle_offer(game, player, player_box, recent_values, cur_turn, random_generator)
        if accepted:
            break
        cur_turn = utils.play_turn(game, player, cur_turn, turn_count, recent_values)
    # finale della partita: rimangono solo il pacco del giocatore e un ultimo pacco. Il dottore fa la sua ultima offerta
    if len(game.remaining) == 1:
        print('----- ULTIMA OFFERTA DEL DOTTORE -----')
        offer_counter += 1
        accepted, _ = utils.handle_offer(game, player, player_box, recent_values, cur_turn, random_generator)
        if accepted:
            pass

    # fine partita
    if not player.final_gain:
        player.final_gain = game.boxes[player.box]
    print(f'Il tuo pacco conteneva: {game.boxes[player.box]} €')
    print(f'Guadagno finale: {player.final_gain} €')
    # chiede se vuoi rigiocare
    rematch = input('Vuoi giocare ancora? (s/n)\n').strip().lower()
    if rematch.startswith('s'):
        main()
    else:
        exit(0)

if __name__ == '__main__':
    main()
