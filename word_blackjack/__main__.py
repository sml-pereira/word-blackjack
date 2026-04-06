"""Entry point for running Word Blackjack as a package: python -m word_blackjack."""

from word_blackjack.engine import (
    print_initial_statements,
    ask_numb_players,
    ask_numb_games,
    ask_level,
    init_game,
    dict_iteration,
    main_loop,
)


def main():
    """Run the Word Blackjack game."""

    # Print the initial statements and rules about the game.
    print_initial_statements()

    # Ask the number of players.
    numb_players = ask_numb_players()

    # Ask the number of games.
    numb_games = ask_numb_games()

    # Ask the level of difficulty.
    turns_per_player = ask_level()

    # Define the maximum number of turns (players × turns per player).
    numb_turns = numb_players * turns_per_player

    # Initialise the game data structure.
    game_data = init_game(21, numb_players, numb_games, numb_turns)
    game_data["turn_players"] = dict_iteration(
        game_data["numb_players"],
        game_data["numb_turns"],
        game_data["players"],
    )

    # Run the main game loop.
    main_loop(game_data)


if __name__ == "__main__":
    main()
