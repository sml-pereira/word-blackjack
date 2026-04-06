# All the functions required for the game are defined in this file!
# Written in Python 3.
# PEP8 style guide for Python code.

import os
import random


# 1) Function that prints the initial statements and informations about the game.
def print_initial_statements():
    """ print_initial_statements() prints:
            a)the name and version of the game;
            b)all the information and rules required to play;
            c)the message that initiate the game."""
    for i in range(7):
        if i == 1 or i == 3 or i == 5 or i == 6:
            print("")
        elif i == 0:
            print("Word Blackjack v1.0")
        elif i == 2:
            print("Game Description:")
            print("")
            print("The game starts with a random letter from A to Z. Each player, plays in its turn. In the first")
            print("play, the first player must say a valid word that starts with the previous random letter.")
            print("Number of points:")
            print("1: You earn 1 point when your word starts with the same letter as the previous valid word.")
            print("3: You earn 3 points when your word rhymes with the previous valid word (same last 3 letters).")
            print("7: You earn 7 points with the combination of the previous rules.")
            print("Victory condition:")
            print("Each game ends with one winner only when any of the players reaches or surpasses 21 points.")
            print("")
            print("Other important rules:")
            print("When the game starts you will be asked to choose the number of players (up to a maximum of 7),")
            print("the number of games to play (an odd number between 1 and 7), and also the level of difficulty.")
            print("In level 1, each player will have 20 turns to reach the maximum score, in level 2, 10 turns, and,")
            print("in level 3, 5 turns only.")
            print("If at the end of the turns no one reaches the maximum score the game ends if you choose to play 1 ")
            print("game, or restarts, if you choose several games!")
            print("Keep also in mind that I DO NOT accept previously written words!")
        else:
            print("Let's start!")


# 2) Function that asks the number of players.
def ask_numb_players():
    """ ask_numb_players() asks to the user the number of players to play the game and decides what to do when the user
        selects letters or an invalid number of players (less than 2 or more than 7 players)."""
    a = 0
    while a <= 1 or a > 7:
        a = str(input("Number of players?"))
        if a.isalpha():
            print("That's not a number...")
            a = 0
        else:
            a = int(a)
            if 1 < a <= 7:
                break
            elif a <= 1:
                print("That's not a valid number of players")
            elif a > 7:
                print("Please choose up to a maximum of 7 players!")
    print("")
    return a


# 3) Function that asks the number of games.
def ask_numb_games():
    """ ask_numb_games() asks to the user the number of games to play and forces an odd number in order to prevent
        any draw situation. It also decides what to do when the user selects letters or an invalid number of games."""
    b = 0
    while b <= 0 or b > 7 or b % 2 == 0:
        b = str(input("Number of games?"))
        if b.isalpha():
            print("That's not a number...")
            b = 0
        else:
            b = int(b)
            if 0 < b <= 7 and b % 2 != 0:
                break
            elif b % 2 == 0:
                print("The number you wrote is not an odd number.")
            elif b <= 0:
                print("That's not a valid number of games")
            elif b > 7:
                print("Please choose up to a maximum of 7 games!")
    print("")
    return b


# 4) Function that asks the level of difficulty:
def ask_level():
    """ ask_level() asks the user the level of difficulty of the game and returns an integer to multiply by the
        number of players.
        It also decides what to do when the user selects letters or an invalid number of difficulty."""
    a = 0
    while a <= 0 or a > 3:
        a = str(input("Choose difficulty (1/2/3)?"))
        if a.isalpha():
            print("That's not a number...")
            a = 0
        else:
            a = int(a)
            if a == 1:
                print("")
                return 20
            elif a == 2:
                print("")
                return 10
            elif a == 3:
                print("")
                return 5
            else:
                print("Please choose the options 1, 2 or 3!")


# 5) Function that initiates the "game_data" data structure.
def init_game(max_points, number_players, number_games, number_turns):
    """ init_game() creates, in a dictionary, all the lists(most of them empty) or integers required to run the game.
        It receives as arguments:
            a)the maximum number of points required to win one game (typically 21 points);
            b)the number of players;
            c)the number of games to be played;
            d)the maximum number of turns in each game."""
    x = 0
    max_score = max_points
    numb_players = number_players
    numb_games = number_games
    numb_turns = number_turns
    turn_counter = 0
    players = []
    scores = []
    total_scores = []
    game_wins = []
    rand_letters = []
    words = []
    valid_words = []
    inv_words = []
    new_word = "none"
    prev_word = "none"

    while x < number_players:
        players.append("Player ")
        players[x] = players[x] + str(x + 1)
        scores.append([0])
        total_scores.append(0)
        game_wins.append(0)
        words.append("")
        inv_words.append("")
        x = x + 1

    initial_data = {"max_score": max_score, "numb_players": numb_players, "numb_games": numb_games,
                    "numb_turns": numb_turns, "turn_counter": turn_counter, "players": players, "scores": scores,
                    "total_scores": total_scores, "game_wins": game_wins, "rand_letters": rand_letters, "words": words,
                    "valid_words": valid_words, "inv_words": inv_words, "new_word": new_word, "prev_word": prev_word}
    return initial_data


# 6) Function that prints every single element in the game_data structure.
def debug_game(game_data):
    """ debug_game() receives as an argument the dictionary game_data previously created and prints all his elements"""
    print("")
    for key in game_data:
        print("%s: %s" % (key, game_data[key]))


# 7) Function that resets the game_data structure elements that require resetting, after one game is played.
def reset_game_data(game_data):
    """ reset_game_data() restores the initial values of several elements in the game_data dictionary.
        It restores the values of the turn_counter, scores, total_scores, words, valid_words, inv_words and new_word.
        This is usefull to restart a new game and store his new information.
        Receives as an argument the game_data dictionary."""
    x = 0
    game_data["turn_counter"] = 0
    game_data["scores"] = []
    game_data["total_scores"] = []
    game_data["words"] = []
    game_data["valid_words"] = []
    game_data["inv_words"] = []
    game_data["new_word"] = "none"

    while x < game_data["numb_players"]:
        game_data["scores"].append([0])
        game_data["total_scores"].append(0)
        game_data["words"].append("")
        game_data["inv_words"].append("")
        x = x + 1


# 8) Function thar iterates between the number of players
def iteration(number_players):
    """ iteration() toggles between the number of players in the game. For instance, if the game has 4 players, it is
        constantly generating 4 values like, 01230123.... when called the next() function.
        It receives as an argument the total number of players in the game."""
    x = []
    for i in range(number_players):
        x.append(i)
    while True:
        for i in x:
            yield i


# 9) Function that creates the turn_players dictionary.
def dict_iteration(number_players, number_turns, players):
    """ dict_iteration() creates one dictionary called turn_players that antecipates to wich player is related each one
        of the turns. This new dictionary is afterwards appended to game_data structure.
        It receives as arguments:
            a)the number of players in the game;
            b)the maximum number of turns to be played;
            c)the list players."""
    turn_players = {}
    iterator = iteration(number_players)
    for i in range(1, (int(number_turns) + 1)):
        turn_players[i] = players[next(iterator)]
    return turn_players


# 10) Function that makes more the repetition of the generated random letters.
def rand_letters_rep(r, game_data):
    """ rand_letters_rep() checks if the new generated random letter exists in the random letters list, and, if so,
        generates another one making the repetition more unplausible.
        It receives as arguments the last random letter generated and the game_data dictionary."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if r in game_data["rand_letters"]:
        s = random.choice(alphabet)
        return s
    else:
        return r


# 11) Function that manages the main loop of the game.
def main_loop(game_data):
    """ main_loop() decides what hapens if the users decide to play just one game or several games, and, in both
        situations, it generates one random letter.
        This loop is also responsible for the repetition of the several games choosen by the users. It also prints the
        final stats and the final message, as well as prevents the repetition of the generated random letters.
        It receives as an argument the game_data dictionary"""
    if game_data["numb_games"] == 1:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = random.choice(alphabet)
        game_data["rand_letters"].append(r)
        game_data["prev_word"] = str(r) + "    "
        turn_loop(game_data)
        turn_results_one_game(game_data)
        print("Please come back fast!")
    else:
        while max(game_data["game_wins"]) != int((game_data["numb_games"] + 1) / 2):
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            r = random.choice(alphabet)
            r = rand_letters_rep(r, game_data)
            game_data["rand_letters"].append(r)
            game_data["prev_word"] = str(r) + "    "
            reset_game_data(game_data)
            print("Game results: ", *(game_data["game_wins"]))
            print("")
            turn_loop(game_data)
            turn_results_several_games(game_data)

        print("")
        print("Game results: ", *(game_data["game_wins"]))
        print("Amazing!", game_data["players"][game_data["game_wins"].index(max(game_data["game_wins"]))],
              "is the WordBlackjack CHAMPION!!!!!!!")
        print("")
        print("Please, come back fast!!")


# 12) Function that manages the turn loop.
def turn_loop(game_data):
    """ turn_loop() is the function that is systematically  asking the players for new words. It is also constantly
        updating the dictionary game_data with the info written by the users.
        It also decides what to do with the word or option written by printing the information asked or by analysing
        the new word.
        It receives as an argument the game_data dictionary."""
    while game_data["turn_counter"] < game_data["numb_turns"]:
        game_data["turn_counter"] = game_data["turn_counter"] + 1
        print(game_data["prev_word"], "    Scores:", *(game_data["total_scores"]))
        a = str(input(game_data["turn_players"][game_data["turn_counter"]] + " say a word or option (l/s/q):"))
        game_data["new_word"] = a
        game_data["new_word"] = game_data["new_word"].lower()
        game_data["prev_word"] = game_data["prev_word"].lower()
        if len(game_data["new_word"]) == 1:
            if game_data["new_word"] == "s" or game_data["new_word"] == "l":
                process_option(game_data)
                game_data["turn_counter"] = game_data["turn_counter"] - 1
            elif game_data["new_word"] == "q":
                process_option(game_data)
                break
            else:
                print("Not a valid word! You lost your turn.")
                upd_inv_words(game_data)
                print("")
        else:
            read_word(game_data)
        x = False
        for i in range(game_data["numb_players"]):
            if game_data["total_scores"][i] >= game_data["max_score"]:
                x = True
        if x:
            break


# 13) Function that manages the results when the player chooses just one game (victory or draw situations).
def turn_results_one_game(game_data):
    """ turn_results_one_game() is the function that prints the game final stats and messages.
        It takes also into account the possibility of draw situations when the maximum number of turns is reached.
        It receives as an argument the game_data dictionary."""
    list_to_compare = []
    for i in range(len(game_data["total_scores"])):
        list_to_compare.append(game_data["total_scores"][i])
    del list_to_compare[game_data["total_scores"].index(max(game_data["total_scores"]))]

    if max(game_data["total_scores"]) == max(list_to_compare):
        print("Turn results:")
        print("")
        print_stats(game_data)
        print("I'm sorry, but there is no winner. Two or more players drew!")
    else:
        print("Turn results:")
        print("")
        print_stats(game_data)
        print("Congratulations!",
              game_data["players"][game_data["total_scores"].index(max(game_data["total_scores"]))],
              "won this game!!")
        print("")
        game_data["game_wins"][game_data["total_scores"].index(max(game_data["total_scores"]))] = \
            game_data["game_wins"][game_data["total_scores"].index(max(game_data["total_scores"]))] + 1


# 14) Function that manages the results when one game ends if the player chooses to play several games.
def turn_results_several_games(game_data):
    """ turn_results_several_games() is the function that prints the game final stats and messages.
        It takes also into account the possibility of draw situations when the maximum number of turns is reached.
        It receives as an argument the game_data dictionary."""
    if game_data["turn_counter"] == game_data["numb_turns"]:
        print("Turn results:")
        print("")
        print_stats(game_data)
        print("I'm sorry, but there is no winner in this game. No one reached the maximum score! Let's try again...")
    else:
        print("Turn results:")
        print("")
        print_stats(game_data)
        print("Congratulations!",
              game_data["players"][game_data["total_scores"].index(max(game_data["total_scores"]))],
              "won this game!!")
        print("")
        game_data["game_wins"][game_data["total_scores"].index(max(game_data["total_scores"]))] = \
            game_data["game_wins"][game_data["total_scores"].index(max(game_data["total_scores"]))] + 1


# 15) Function that updates the game_data structure when the user writes an invalid word.
def upd_inv_words(game_data):
    """ upd_inv_words() receives as an argument the game_data dictionary and updates the respective elements when an
        invalid word is written by the players."""
    game_data["scores"][int((game_data["turn_players"][game_data["turn_counter"]][7])) - 1].append(0)
    game_data["inv_words"][int((game_data["turn_players"][game_data["turn_counter"]][7])) - 1] = \
        game_data["inv_words"][int((game_data["turn_players"][game_data["turn_counter"]][7])) - 1] \
        + game_data["new_word"] + ", "


# 16) Function that updates the game_data structure when the user writes a valid word.
def upd_val_words(game_data, n):
    """ upd_val_words() receives as arguments the game_data dictionary and the number of points gained by the player
        in one turn.
        It also updates the respective elements in the game_data structure when a valid word is written."""
    game_data["scores"][int((game_data["turn_players"][game_data["turn_counter"]][7])) - 1].append(n)
    game_data["total_scores"][int((game_data["turn_players"][game_data["turn_counter"]][7])) - 1] = \
        sum(game_data["scores"][int((game_data["turn_players"][game_data["turn_counter"]][7])) - 1])
    game_data["words"][int((game_data["turn_players"][game_data["turn_counter"]][7])) - 1] = \
        game_data["words"][int((game_data["turn_players"][game_data["turn_counter"]][7])) - 1] + \
        game_data["new_word"] + ", "
    game_data["valid_words"].append(game_data["new_word"])
    game_data["prev_word"] = game_data["new_word"]


# 17) Function that reads the last word written.
def read_word(game_data):
    """ read_word() checks if the word written has 0 or 2 letters and decides that it is invalid.
        If the word has 3 or more letters channels it to the verify_existance function.
        It receives as an argument the game_data dictionary."""
    if len(game_data["new_word"]) == 0 or len(game_data["new_word"]) == 2:
        print("Not a valid word! You lost your turn.")
        upd_inv_words(game_data)
        print("")
    else:
        verify_existance(game_data)


# 18) Function that verifies if the word written is a valid English word.
def verify_existance(game_data):
    """ verify_existance() checks if the last word written exists in an external text file with all the English words.
        If the word is in the list this function channels it to the verify_2() function, and, if not, decides that the
        word is invalid.
        It receives as an argument the game_data dictionary."""
    word_list_path = os.path.join(os.path.dirname(__file__), "data", "english_words.txt")
    f = open(word_list_path, "r")
    s = f.read()
    if game_data["new_word"] in s:
        verify_repetition(game_data)
    else:
        print("Not a valid word! You lost your turn.")
        upd_inv_words(game_data)
        print("")
    f.close()


# 19) Function that verifies if the last word has been written before.
def verify_repetition(game_data):
    """ verify_repetition() checks if the word has already been used.
        If the word is valid it channels it to the process_word() function.
        It receives as an argument the game_data dictionary."""
    if game_data["new_word"] in game_data["valid_words"]:
        print("This word has already been used! You lost your turn")
        upd_inv_words(game_data)
        print("")
    else:
        process_word(game_data)


# 20) Function that processes the results when a valid word is written by any of the players.
def process_word(game_data):
    """ process_word() decides when a word should receive 7, 3 or 1 points.
        It also updates the respective elements in the game_data and prints the message of the points earned.
        It receives as an argument the game_data dictionary."""
    if game_data["new_word"][0] == game_data["prev_word"][0] \
            and game_data["new_word"][-1] == game_data["prev_word"][-1] \
            and game_data["new_word"][-2] == game_data["prev_word"][-2] \
            and game_data["new_word"][-3] == game_data["prev_word"][-3]:
        print("Fantastic!!!!!!! 7 points!!!!!!!")
        upd_val_words(game_data, 7)
        print("")
    elif game_data["new_word"][-1] == game_data["prev_word"][-1] \
            and game_data["new_word"][-2] == game_data["prev_word"][-2] \
            and game_data["new_word"][-3] == game_data["prev_word"][-3]:
        print("Good one!!! 3 points!!!")
        upd_val_words(game_data, 3)
        print("")
    elif game_data["new_word"][0] == game_data["prev_word"][0]:
        print("Great! 1 point!")
        upd_val_words(game_data, 1)
        print("")
    else:
        print("Not a valid word! You lost your turn.")
        upd_inv_words(game_data)
        print("")


# 21) Function that manages the results when one of the valid options is pressed.
def process_option(game_data):
    """ process_option() channels the results to other 3 diferent functions when the options "l, s, q" are selected.
        It receives as an argument the game_data dictionary."""
    if game_data["new_word"] == "l":
        print_word_list(game_data)
    elif game_data["new_word"] == "s":
        print_stats(game_data)
    elif game_data["new_word"] == "q":
        quit_game(game_data)


# 22) Function that define the results when the option "l" is selected.
def print_word_list(game_data):
    """ print_word_list() prints all the valid words written by the players in the previous turns.
        It receives as an argument the game_data dictionary."""
    if game_data["turn_counter"] == 1:
        print("List of Words:")
        for i in range(len(game_data["players"])):
            print(game_data["players"][i][0] + game_data["players"][i][7] + ": No words written yet, you have",
                  sum(game_data["scores"][i]), "points!")
        print("")
    else:
        print("List of words:")
        for i in range(len(game_data["players"])):
            print(game_data["players"][i][0] + game_data["players"][i][7] + ",", game_data["words"][i] + "You have",
                  sum(game_data["scores"][i]), "points!")
        print("")


# 23) Function that makes it possible to divide by 0
def safe_div(x, y):
    """ safe_div() "allows" division by 0 when assigning quotient = 0.
        It receives as arguments two numbers (x and y), being logically useful for cases where y = 0."""
    if y == 0:
        return 0
    return x / y


# 24) Function that defines the results when the option "s" is selected.
def print_stats(game_data):
    """ print_stats() prints the average number of points of each player.
        It receives as an argument the game_data dictionary."""
    print("Printing Stats:")
    for i in range(len(game_data["players"])):
        print(game_data["players"][i], "average:",
              safe_div(sum(game_data["scores"][i]), (len(game_data["scores"][i]) - 1)), "points per play!")
    print("")


# 25) Function that defines the results when the option "q" is selected.
def quit_game(game_data):
    """ quit_game(), when any of the players press the "q" option, ends the game by printing final stats.
        It receives as an argument the game_data dictionary."""
    print("Final stats:")
    for i in range(len(game_data["players"])):
        print(game_data["players"][i], "won", game_data["game_wins"][i], "games!")
    print("")
    print("Quitting!!")
    print("Please come back fast!!")
