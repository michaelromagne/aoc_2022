"""Advent of code 2022 - Day 14"""
import os
from typing import List, Tuple

INPUT_TXT = os.path.join(os.path.dirname(__file__), "rocks.txt")
SOURCE_POSITION = (500, 0)


def get_sand_position(rocks: str) -> List[Tuple[int, int]]:
    rock_positions = []
    sand_positions = []
    rock_lines_list = rocks.splitlines()
    rocks_list = [
        [rock.split(",") for rock in rock_line.split(" -> ")]
        for rock_line in rock_lines_list
    ]
    for rock_struct in rocks_list:
        for i in range(1, len(rock_struct)):
            if int(rock_struct[i][0]) == int(rock_struct[i - 1][0]):
                rock_positions += [
                    (
                        int(rock_struct[i][0]),
                        rock_y,
                    )
                    for rock_y in range(
                        min(int(rock_struct[i - 1][1]), int(rock_struct[i][1])),
                        max(int(rock_struct[i - 1][1]), int(rock_struct[i][1])) + 1,
                    )
                ]
            else:
                rock_positions += [
                    (
                        rock_x,
                        int(rock_struct[i][1]),
                    )
                    for rock_x in range(
                        min(int(rock_struct[i - 1][0]), int(rock_struct[i][0])),
                        max(int(rock_struct[i - 1][0]), int(rock_struct[i][0])) + 1,
                    )
                ]
    max_y = max([rock_y for _, rock_y in rock_positions])

    while True:
        sand_position = SOURCE_POSITION
        falling = True
        while falling:
            if (
                sand_position[0],
                sand_position[1] + 1,
            ) not in rock_positions + sand_positions:
                sand_position = (sand_position[0], sand_position[1] + 1)
            elif (
                sand_position[0] - 1,
                sand_position[1] + 1,
            ) not in rock_positions + sand_positions:
                sand_position = (sand_position[0] - 1, sand_position[1] + 1)
            elif (
                sand_position[0] + 1,
                sand_position[1] + 1,
            ) not in rock_positions + sand_positions:
                sand_position = (sand_position[0] + 1, sand_position[1] + 1)
            else:
                sand_positions.append(sand_position)
                falling = False

            if sand_position[1] > max_y:
                break
        if sand_position[1] > max_y:
            break
    return set(sand_positions)


def get_sand_position_part_2(rocks: str) -> List[Tuple[int, int]]:
    rock_positions = []
    sand_positions = []
    rock_lines_list = rocks.splitlines()
    rocks_list = [
        [rock.split(",") for rock in rock_line.split(" -> ")]
        for rock_line in rock_lines_list
    ]
    for rock_struct in rocks_list:
        for i in range(1, len(rock_struct)):
            if int(rock_struct[i][0]) == int(rock_struct[i - 1][0]):
                rock_positions += [
                    (
                        int(rock_struct[i][0]),
                        rock_y,
                    )
                    for rock_y in range(
                        min(int(rock_struct[i - 1][1]), int(rock_struct[i][1])),
                        max(int(rock_struct[i - 1][1]), int(rock_struct[i][1])) + 1,
                    )
                ]
            else:
                rock_positions += [
                    (
                        rock_x,
                        int(rock_struct[i][1]),
                    )
                    for rock_x in range(
                        min(int(rock_struct[i - 1][0]), int(rock_struct[i][0])),
                        max(int(rock_struct[i - 1][0]), int(rock_struct[i][0])) + 1,
                    )
                ]
    max_y = max([rock_y for _, rock_y in rock_positions])
    rock_positions += [
        (
            rock_x,
            max_y + 2,
        )
        for rock_x in range(
            -1000,
            1000,
        )
    ]
    while True:
        sand_position = SOURCE_POSITION
        falling = True
        while falling:
            if (
                sand_position[0],
                sand_position[1] + 1,
            ) not in rock_positions + sand_positions:
                sand_position = (sand_position[0], sand_position[1] + 1)
            elif (
                sand_position[0] - 1,
                sand_position[1] + 1,
            ) not in rock_positions + sand_positions:
                sand_position = (sand_position[0] - 1, sand_position[1] + 1)
            elif (
                sand_position[0] + 1,
                sand_position[1] + 1,
            ) not in rock_positions + sand_positions:
                sand_position = (sand_position[0] + 1, sand_position[1] + 1)
            else:
                if sand_position == SOURCE_POSITION:
                    sand_positions.append(SOURCE_POSITION)
                    return sand_positions
                sand_positions.append(sand_position)
                falling = False


def main():
    with open(INPUT_TXT) as f:
        rocks = f.read()
    sand_positions = get_sand_position(rocks)
    print(len(sand_positions))
    sand_positions_part_2 = get_sand_position_part_2(rocks)
    print(len(sand_positions_part_2))


if __name__ == "__main__":
    raise SystemExit(main())
