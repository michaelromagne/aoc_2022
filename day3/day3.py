#!/usr/bin/env python3

"""Advent of code 2022 - Day 3"""

from string import ascii_lowercase

with open("rucksack_inventory.txt", "r") as rucksack_inventory:
    rucksack_inventory = rucksack_inventory.read()
rucksack_list = rucksack_inventory.split("\n")

# Part 1

rucksack_compartiments = [
    (set(rucksack[: len(rucksack) // 2]), set(rucksack[len(rucksack) // 2 :]))
    for rucksack in rucksack_list
]

rucksack_misplaced_objects = [
    next(iter(compartiment_1.intersection(compartiment_2)))
    for compartiment_1, compartiment_2 in rucksack_compartiments
]

object_priorities = {letter: id for id, letter in enumerate(ascii_lowercase, start=1)}
object_priorities.update(
    {letter.upper(): id for id, letter in enumerate(ascii_lowercase, start=27)}
)

rucksack_priorities = [
    object_priorities[object_type] for object_type in rucksack_misplaced_objects
]

print(f"Rucksack misplaced objects priorities : {sum(rucksack_priorities)}")

# Part 2

rucksack_objects = [set(rucksack) for rucksack in rucksack_list]

group_badge_list = [
    next(
        iter(
            rucksack_objects[i].intersection(
                rucksack_objects[i + 1], rucksack_objects[i + 2]
            )
        )
    )
    for i in range(0, len(rucksack_objects), 3)
]

group_priorities = [object_priorities[object_type] for object_type in group_badge_list]

print(f"Group badges priority: {sum(group_priorities)}")
