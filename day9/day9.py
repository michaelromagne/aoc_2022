"""Advent of code 2022 - Day 9"""
from __future__ import annotations

import os
import numpy as np
from typing import Optional

INPUT_TXT = os.path.join(os.path.dirname(__file__), "head_motions.txt")

HEAD_MOTION_MAP = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


class Knot:
    def __init__(self):
        self.previous_knot_position = (0, 0)
        self.knot_visited_positions = [(0, 0)]

    def get_knot_position(self):
        x_knot, y_knot = self.knot_visited_positions[-1]
        delta_x = self.previous_knot_position[0] - x_knot
        delta_y = self.previous_knot_position[1] - y_knot

        if abs(delta_x) >= 2:
            x_knot = self.knot_visited_positions[-1][0] + np.sign(delta_x)
            if abs(delta_y) >= 1:
                y_knot = self.knot_visited_positions[-1][1] + np.sign(delta_y)
        if abs(delta_y) >= 2:
            y_knot = self.knot_visited_positions[-1][1] + np.sign(delta_y)
            if abs(delta_x) >= 1:
                x_knot = self.knot_visited_positions[-1][0] + np.sign(delta_x)
        self.knot_visited_positions.append((x_knot, y_knot))

    def move_head(self, direction: str, n_moves: int, previous_knot: Optional[Knot]):
        if previous_knot is None:
            for _ in range(n_moves):
                self.previous_knot_position = (
                    self.previous_knot_position[0] + HEAD_MOTION_MAP[direction][0],
                    self.previous_knot_position[1] + HEAD_MOTION_MAP[direction][1],
                )
                self.get_knot_position()
        else:
            for x_prev_knot, y_prev_knot in previous_knot.knot_visited_positions[
                -n_moves:
            ]:
                self.previous_knot_position = (x_prev_knot, y_prev_knot)
                self.get_knot_position()


def compute_tail_positions(head_motions: str, n_knots: int):
    head_motions_list = head_motions.splitlines()
    head_motions_list = [head_motion.split(" ") for head_motion in head_motions_list]

    knot_list = [Knot() for _ in range(1, n_knots)]
    for direction, n_moves in head_motions_list:
        for i in range(0, n_knots - 1):
            if i == 0:
                knot_list[i].move_head(direction, int(n_moves), previous_knot=None)
            else:
                knot_list[i].move_head(
                    direction, int(n_moves), previous_knot=knot_list[i - 1]
                )
    tail_visited_positions = knot_list[-1].knot_visited_positions
    tail_visited_positions_set = set(tail_visited_positions)
    return tail_visited_positions_set


def main():
    with open(INPUT_TXT) as f:
        head_motions = f.read()
    knot_positions_set_1_knot = compute_tail_positions(head_motions, 2)
    print(
        f"Number of visited positions by the knot with 1 knot: {len(knot_positions_set_1_knot)}"
    )
    knot_positions_set_10_knots = compute_tail_positions(head_motions, 10)
    print(
        f"Number of visited positions by the knot with 10 knots: {len(knot_positions_set_10_knots)}"
    )


if __name__ == "__main__":
    raise SystemExit(main())
