import random
# this script is supposed for 8 players, and overall there will be 7 games for each player to play with each other
# These 3 lists : players, main_list_1 and main_list_2  are our main list from which we will create players for each games.
# add global function which will be added to the game_6_or_8_players.py
def find_8_game_players_func():

    untouch_players = ['Ayaz', 'Mariyam','Rufat', 'Eugenia', 'Tanya', 'Krstyna', 'Piotr', 'Guna']  # do not change this list
    players = random.sample(untouch_players, 8)  # and here we randomly creating a new list of players
    main_list_1 = []
    main_list_2 = []
    # *******************
    # creating main_list_1 from players list
    main_list_1[0:1] = players[0:2]
    main_list_1[2:3] = players[4:6]
    main_list_1[4:5] = players[2:4]
    main_list_1[6:7] = players[6:]
    # creating main_list_2 from players list
    main_list_2[0:1] = players[0:2]
    main_list_2[2:3] = players[6:]
    main_list_2[4:5] = players[2:6]

    # this function helps to indetify game 1 players from list : players
    def first_game_players():
        game_1_players = []
        i = 0
        while i < len(players) - 1:  # when < 7
            game_1_players.append(players[i] + ' - ' + players[i+1])
            i += 2
        return game_1_players

    # this function helps to indetify game 2, 4, 6 players from list : players, main_list_1 and main_list_2
    # for 2, 4, 6 games players, lists indexes are 0-2 , 1-3, 4-6, 5-7
    def rest_games_players_1(mylist):
        game_2_4_6_players = []
        i = 0
        while i < len(players):
            if i == 0:
                game_2_4_6_players.append(mylist[i] + ' - ' + mylist[i+2])
            elif i == 1:
                game_2_4_6_players.append(mylist[i] + ' - ' + mylist[i+2])
            elif i == 4:
                game_2_4_6_players.append(mylist[i] + ' - ' + mylist[i+2])
            elif i == 5:
                game_2_4_6_players.append(mylist[i] + ' - ' + mylist[i+2])
            i += 1
        return(game_2_4_6_players)

    # this function helps to indetify game 3, 5, 7 players from list : players, main_list_1 and main_list_2
    # for 3, 5, 7 games players, lists indexes are 0-3 , 1-2, 4-7, 5-6
    def rest_games_players_2(mylist):
        game_3_5_7_players = []
        i = 0
        while i < len(players):
            if i == 0:
                game_3_5_7_players.append(mylist[i] + ' - ' + mylist[i+3])
            elif i == 1:
                game_3_5_7_players.append(mylist[i] + ' - ' + mylist[i+1])
            elif i == 4:
                game_3_5_7_players.append(mylist[i] + ' - ' + mylist[i+3])
            elif i == 5:
                game_3_5_7_players.append(mylist[i] + ' - ' + mylist[i+1])
            i += 1
        return(game_3_5_7_players)


    return '*Game 1 players, 0-30 mins:*' + '\n' + ', '.join(first_game_players()) + '\n' + \
           '*Game 2 players, 30-45 mins:*' + '\n' + ', '.join(rest_games_players_1(players)) + '\n' + \
           '*Game 3 players, 45-60 mins:*' + '\n' + ', '.join(rest_games_players_2(players)) + '\n' + \
           '*Game 4 players, 60-75 mins:*' + '\n' + ', '.join(rest_games_players_1(main_list_1)) + '\n' + \
           '*Game 5 players, 75-90 mins:*' + '\n' + ', '.join(rest_games_players_2(main_list_1)) + '\n' + \
           '*Game 6 players, 90-105 mins:*' + '\n' + ', '.join(rest_games_players_1(main_list_2)) + '\n' + \
           '*Game 7 players, 105-120 mins:*' + '\n' + ', '.join(rest_games_players_2(main_list_2)) + '\n'


#print(find_8_game_players_func())
