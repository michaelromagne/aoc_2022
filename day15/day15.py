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
    min_col: int = -100000000,
    max_col: int = +100000000,
    filter_baecon: bool = True,
) -> List[Tuple[int, int]]:
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
        for x in range(
            max(min_col, sensor[0] - distance),
            min(max_col + 1, sensor[0] + distance + 1),
        ):
            if manhattan_distance(sensor[0], sensor[1], x, row) <= distance:
                scanned_positions.append((x, row))
    if filter_baecon:
        return set(scanned_positions) - set(baecon_positions)
    return set(scanned_positions)


def get_tuning_frequency(
    sensors: str,
    grid_min: int,
    grid_max: int,
) -> int:
    for row in range(grid_min, grid_max + 1):
        scanned_positions = get_scanned_positions_in_row(
            sensors,
            row=row,
            min_col=grid_min,
            max_col=grid_max,
            filter_baecon=False,
        )
        print(f"Scan done for row {row}")
        for x in range(grid_min, grid_max + 1):
            if (x, row) not in scanned_positions:
                print(f"Solution with x = {x} and and y = {row}")
                return x * 4000000 + row
        print("No solution here...")


def main():
    with open(INPUT_TXT) as f:
        sensors = f.read()
    scanned_positions = get_scanned_positions_in_row(sensors, 2000000)
    print(len(scanned_positions))
    tuning_frequency = get_tuning_frequency(
        sensors,
        grid_min=0,
        grid_max=4000000,
    )
    print(tuning_frequency)


if __name__ == "__main__":
    raise SystemExit(main())
