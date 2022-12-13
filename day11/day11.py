"""Advent of code 2022 - Day 11"""
import operator
import os
from typing import List

INPUT_TXT = os.path.join(os.path.dirname(__file__), "monkey_list.txt")

# There are only add and multiply operators in this problem
OPERATORS = {
    "+": operator.add,
    "*": operator.mul,
}


def compute_new_worry_level(old_worry_level, oper, factor, worry_divider):
    old_worry_level, factor = int(old_worry_level), int(
        factor
    ) if factor != "old" else int(old_worry_level)
    return OPERATORS[oper](old_worry_level, factor) // worry_divider


def compute_monkey_business(
    monkey_objects: str,
    n_rounds: int,
    worry_divider: int = 3,
) -> int:
    monkey_objects_list = [
        monkey.split("\n") for monkey in monkey_objects.split("\n\n")
    ]
    monkey_split_list = [
        [
            monkey[1][18:].split(", "),
            monkey[2][23:].split(),
            monkey[3][21:],
            monkey[4][29:],
            monkey[5][30:],
        ]
        for monkey in monkey_objects_list
    ]
    monkey_objects_counters = [0] * len(monkey_objects_list)

    # PPCM to avoid overflow
    PPCM = 1
    for monkey in monkey_split_list:
        PPCM *= int(monkey[2])

    for r in range(n_rounds):
        # print(f"Round {r}")
        for i, monkey in enumerate(monkey_split_list):
            objects_to_throw = monkey[0].copy()
            monkey_objects_counters[i] += len(objects_to_throw)
            monkey[0] = []
            for object_worry_level in objects_to_throw:
                new_worry_level = (
                    compute_new_worry_level(
                        object_worry_level,
                        monkey[1][0],
                        monkey[1][1],
                        worry_divider,
                    )
                    % PPCM
                )
                if new_worry_level % int(monkey[2]) == 0:
                    monkey_split_list[int(monkey[3])][0].append(new_worry_level)
                else:
                    monkey_split_list[int(monkey[4])][0].append(new_worry_level)
    two_most_important_monkeys = sorted(monkey_objects_counters)[-2:]
    return two_most_important_monkeys[0] * two_most_important_monkeys[1]


def main():
    with open(INPUT_TXT) as f:
        monkey_objects = f.read()
    monkey_business = compute_monkey_business(monkey_objects, 20, 3)
    print(f"Monkey business after 20 rounds : {monkey_business}")
    monkey_business = compute_monkey_business(monkey_objects, 10000, 1)
    print(f"Calm down ! Monkey business after 10000 rounds : {monkey_business}")


if __name__ == "__main__":
    raise SystemExit(main())
