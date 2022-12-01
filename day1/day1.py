#!/usr/bin/env python3

"""Advent of code 2022 - Day 1"""

with open("elves_food.txt", "r") as elves_food:
    elves_all_food = elves_food.read()

# Part 1 - Who's the strongest elve ?

food_string_list = [food.split("\n") for food in elves_all_food.split("\n\n")]
# Prepend "0" to food string to avoid exception when a blank line is at the end of the file
food_list = [[int("0"+food) for food in food_list] for food_list in food_string_list]
sum_food_per_elve = [sum(food_elve) for food_elve in food_list]
max_food = max(sum_food_per_elve)
print(f"Total calories for the strongest elve : {max_food}")

# Part 2 - Two elves in backup

sorted_sum_food = sorted(sum_food_per_elve)
sum_three_strongest_elves = sum(sorted_sum_food[-3:])
print(f"Total calories for the three strongest elves : {sum_three_strongest_elves}")
