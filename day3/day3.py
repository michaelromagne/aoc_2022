"""Advent of code 2022 - Day 3"""

import os
from string import ascii_lowercase
from typing import Dict

INPUT_DAY3 = os.path.join(os.path.dirname(__file__), "rucksack_inventory.txt")

OBJECTS_PRIORITIES = {letter: id for id, letter in enumerate(ascii_lowercase, start=1)}
OBJECTS_PRIORITIES.update(
    {letter.upper(): id for id, letter in enumerate(ascii_lowercase, start=27)}
)


def sum_misplaced_objects_priorities(
    rucksack_inventory: str,
    objects_priorities: Dict[str, int],
):
    rucksack_list = rucksack_inventory.split("\n")
    rucksack_compartiments = [
        (set(rucksack[: len(rucksack) // 2]), set(rucksack[len(rucksack) // 2 :]))
        for rucksack in rucksack_list
    ]
    rucksack_misplaced_objects = [
        next(iter(compartiment_1.intersection(compartiment_2)))
        for compartiment_1, compartiment_2 in rucksack_compartiments
    ]
    rucksack_priorities = [
        objects_priorities[object_type] for object_type in rucksack_misplaced_objects
    ]
    return sum(rucksack_priorities)


def sum_group_badges_priorities(
    rucksack_inventory: str,
    objects_priorities: Dict[str, int],
):
    rucksack_list = rucksack_inventory.split("\n")
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
    group_priorities = [
        objects_priorities[object_type] for object_type in group_badge_list
    ]
    return sum(group_priorities)


def main():
    with open(INPUT_DAY3, "r") as rucksack_inventory:
        rucksack_inventory = rucksack_inventory.read()
    print(
        f"Rucksack misplaced objects priorities : {sum_misplaced_objects_priorities(rucksack_inventory,OBJECTS_PRIORITIES)}"
    )

    print(
        f"Group badges priority: {sum_group_badges_priorities(rucksack_inventory,OBJECTS_PRIORITIES)}"
    )


if __name__ == "__main__":
    raise SystemExit(main())
