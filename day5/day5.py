"""Advent of code 2022 - Day 5"""

import os
from typing import Dict

INPUT_TXT = os.path.join(os.path.dirname(__file__), "crates_rearrangement.txt")


def get_initial_setup(crates_setup: str, n_stacks: int) -> Dict[int, str]:
    """Parse string to return a dictionary representing initial setup."""
    crates_setup_dict = {i + 1: "" for i in range(n_stacks)}

    for line in crates_setup.splitlines():
        if "[" not in line:
            break
        for i in range(n_stacks):
            if line[i * 4 + 1] != " ":
                crates_setup_dict[i + 1] += line[i * 4 + 1]
    return crates_setup_dict


def rearrange_crates(setup: Dict[int, str], strategy: str, part: int) -> str:
    """Rearrange crates according to strategy and return final top crates."""
    if part not in [1, 2]:
        raise ValueError("Part not known !")
    for line in strategy.splitlines():
        n_crates_to_move, start_stack, end_stack = (
            int(line.split(" ")[1]),
            int(line.split(" ")[3]),
            int(line.split(" ")[5]),
        )
        crates_to_move = setup[start_stack][:n_crates_to_move]
        if part == 1:
            crates_to_move = crates_to_move[::-1]
        setup[start_stack] = setup[start_stack][n_crates_to_move:]
        setup[end_stack] = crates_to_move + setup[end_stack]
        top_crates = ""
    for stack in setup.values():
        top_crates += stack[0]
    return top_crates


def main():

    with open(INPUT_TXT) as f:
        file = f.read().split("\n\n")
        n_stacks = int(file[0].split("\n")[-1][-2])
        if len(file) != 2:
            raise ValueError("Wrong input file format !")
        initial_setup = get_initial_setup(file[0], n_stacks)
        print(rearrange_crates(initial_setup.copy(), file[1], 1))
        print(rearrange_crates(initial_setup.copy(), file[1], 2))


if __name__ == "__main__":
    raise SystemExit(main())
