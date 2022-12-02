#!/usr/bin/env python3

"""Advent of code 2022 - Day 1"""

from typing import List

with open("elves_food.txt", "r") as elves_food:
    elves_all_food = elves_food.read()


food_string_list = [food.split("\n") for food in elves_all_food.split("\n\n")]
# Prepend "0" to food string to avoid exception when a blank line is at the end of the file
food_list = [[int("0" + food) for food in food_list] for food_list in food_string_list]


# Part 1 - Who's the strongest elve ?


def get_strongest_elves_calories(
    food_list: List[List[int]],
    n_elves: int,
):
    """Get calories carried by the n strongest elves."""
    if n_elves < 1:
        raise ValueError("You should have n_elves greater than 1 !")
    sum_food_per_elve = [sum(food_elve) for food_elve in food_list]
    sorted_sum_food = sorted(sum_food_per_elve)
    sum_strongest_elves = sum(sorted_sum_food[-n_elves:])
    print(
        f"Total calories for the {n_elves} strongest elve{'s' if n_elves>1 else ''} : {sum_strongest_elves}"
    )


get_strongest_elves_calories(food_list, 1)

# Part 2 - Two elves in backup
get_strongest_elves_calories(food_list, 3)
