#!/usr/bin/env python3

"""Advent of code 2022 - Day 1"""

from typing import List, Tuple

with open("game_strategy.txt", "r") as game_strategy:
    game_strategy = game_strategy.read()

game_list = [tuple(game.split(" ")) for game in game_strategy.split("\n")]

# Part 1


def rock_paper_scissors_game(game: Tuple[str, str]):
    """Give number of points for a single game."""
    puntos = 0
    # Rock
    if game[1] == "X":
        puntos += 1
        if game[0] == "A":
            puntos += 3
        elif game[0] == "C":
            puntos += 6
    # Paper
    elif game[1] == "Y":
        puntos += 2
        if game[0] == "A":
            puntos += 6
        elif game[0] == "B":
            puntos += 3
    # Scissors
    else:
        puntos += 3
        if game[0] == "B":
            puntos += 6
        elif game[0] == "C":
            puntos += 3
    return puntos


def get_total_points(game_list: List[Tuple[str, str]], part: int):
    """Get total points following a game strategy, for part 1 or part 2."""
    if part == 1:
        points_list = [rock_paper_scissors_game(game) for game in game_list]
    elif part == 2:
        points_list = [rock_paper_scissors_game_part_2(game) for game in game_list]
    else:
        raise ValueError("Unknown part !")
    total_points = sum(points_list)
    print(f"Total points following the game strategy : {total_points}")


get_total_points(game_list, 1)

# Part 2


def rock_paper_scissors_game_part_2(game: Tuple[str, str]):
    """Give number of points for a single game."""
    # Lose
    if game[1] == "X":
        if game[0] == "A":
            return 3
        elif game[0] == "B":
            return 1
        else:
            return 2
    # Draw
    elif game[1] == "Y":
        if game[0] == "A":
            return 4
        elif game[0] == "B":
            return 5
        else:
            return 6
    # Win
    else:
        if game[0] == "A":
            return 8
        elif game[0] == "B":
            return 9
        else:
            return 7


get_total_points(game_list, 2)
