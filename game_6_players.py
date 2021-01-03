
import random
# this script is supposed for 8 players, and overall there will be 7 games for each player to play with each other
# These 3 lists : players, main_list_1 and main_list_2  are our main list from which we will create players for each games.

def find_6_game_players_func():

    untouch_players = ['Ayaz', 'Mariyam','Rufat', 'Eugenia', 'Tanya', 'Krstyna']  # do not change this list
    players = random.sample(untouch_players, 6)

    game_1_players = players[0] + ' - ' + players[1] + ', ' + players[2] + ' - ' + players[3] + ', ' + players[4] + ' - ' + players[5]
    game_2_players = players[0] + ' - ' + players[3] + ', ' + players[1] + ' - ' + players[4] + ', ' + players[2] + ' - ' + players[5]
    game_3_players = players[0] + ' - ' + players[2] + ', ' + players[1] + ' - ' + players[5] + ', ' + players[3] + ' - ' + players[4]
    game_4_players = players[0] + ' - ' + players[4] + ', ' + players[1] + ' - ' + players[2] + ', ' + players[3] + ' - ' + players[5]
    game_5_players = players[0] + ' - ' + players[5] + ', ' + players[1] + ' - ' + players[3] + ', ' + players[2] + ' - ' + players[4]



    return '*Game 1 players, 0-30 mins:*' + '\n' + game_1_players + '\n' + \
           '*Game 2 players, 30-60 mins:*' + '\n' + game_2_players + '\n' + \
           '*Game 3 players, 60-90 mins:*' + '\n' + game_3_players + '\n' + \
           '*Game 4 players, 90-105 mins:*' + '\n' + game_4_players + '\n' + \
           '*Game 5 players, 105-120 mins:*' + '\n' + game_5_players


find_6_game_players_func()
