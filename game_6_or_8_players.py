from game_6_players import find_6_game_players_func
from game_8_players import find_8_game_players_func

while True:
    user_input = input("Please enter players number (6 or 8) : ")
    if user_input == '6':
        print(find_6_game_players_func())
    elif user_input == '8':
        print(find_8_game_players_func())
    else:
        print('Ooops, wrong input. We expected 6 or 8')
    print('\n' * 2)
