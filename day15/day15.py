"""Advent of code 2022 - Day 15"""
import os
from typing import List, Tuple
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), "sensors.txt")


def manhattan_distance(x1: int, y1: int, x2: int, y2: int):
    return abs(x1 - x2) + abs(y1 - y2)


def get_scanned_positions_in_row(
    sensors: str,
    row: int,
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    sensors_list = sensors.splitlines()
    sensor_positions = []
    baecon_positions = []
    scanned_positions = []
    for sensor in sensors_list:
        m = re.match(
            r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", sensor
        )
        sensor, closest_baecon = (
            (int(m.group(1)), int(m.group(2))),
            (int(m.group(3)), int(m.group(4))),
        )
        baecon_positions += [closest_baecon]
        sensor_positions += [sensor]

        distance = manhattan_distance(*sensor, *closest_baecon)

        if row >= sensor[1]:
            low_bound = sensor[0] + row - sensor[1] - distance
            high_bound = sensor[0] + sensor[1] + distance - row
        else:
            low_bound = sensor[0] - row + sensor[1] - distance
            high_bound = sensor[0] - sensor[1] + row + distance
        if low_bound <= high_bound:
            scanned_positions.append((low_bound, high_bound))

    return scanned_positions, baecon_positions


def get_tuning_frequency(
    sensors: str,
    grid_min: int,
    grid_max: int,
) -> int:
    for row in range(grid_min, grid_max + 1):
        scanned_positions, _ = get_scanned_positions_in_row(
            sensors,
            row=row,
        )
        print(f"Scanning for row {row}...")
        for x in range(grid_min, grid_max + 1):
            if all(
                [
                    (x < low_bound) | (x > high_bound)
                    for low_bound, high_bound in scanned_positions
                ]
            ):
                print(f"Solution with x = {x} and and y = {row}")
                return x * 4000000 + row
        print("No solution here !")


def main():
    with open(INPUT_TXT) as f:
        sensors = f.read()

    ### Part 1

    scanned_positions, baecon_positions = get_scanned_positions_in_row(sensors, 2000000)
    set_positions = set()
    for low_bound, high_bound in scanned_positions:
        set_positions.update(list(range(low_bound, high_bound + 1)))
    for baecon_pos in baecon_positions:
        if baecon_pos[1] == 2000000:
            set_positions.discard(baecon_pos[0])
    print(len(set_positions))

    ### Part 2
    tuning_frequency = get_tuning_frequency(
        sensors,
        grid_min=0,
        grid_max=4000000,
    )
    print(tuning_frequency)


if __name__ == "__main__":
    raise SystemExit(main())
