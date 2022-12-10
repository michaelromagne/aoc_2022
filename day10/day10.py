"""Advent of code 2022 - Day 9"""
import os
from typing import List

INPUT_TXT = os.path.join(os.path.dirname(__file__), "cycles.txt")


def compute_X(cycles: str) -> List[int]:
    X = [1]
    cycles = [cycle.split(" ") for cycle in cycles.splitlines()]
    for cycle in cycles:
        if cycle[0] == "addx":
            new_X = X[-1] + int(cycle[1])
            X += [X[-1], new_X]
        else:
            X += [X[-1]]
    return X


def show_drawing_CRT(cycles: str):
    X = compute_X(cycles)
    pixels = [
        "#" if x in [(i - 1) % 40, i % 40, (i + 1) % 40] else "."
        for i, x in enumerate(X)
    ]
    drawing = "\n".join(["".join(pixels[i * 40 : (i + 1) * 40]) for i in range(6)])
    return drawing


def main():
    with open(INPUT_TXT) as f:
        cycles = f.read()
    X = compute_X(cycles)
    sum_signal_strengths = (
        X[19] * 20
        + X[59] * 60
        + X[99] * 100
        + X[139] * 140
        + X[179] * 180
        + X[219] * 220
    )
    print(f"The sum of signal strengths is : {sum_signal_strengths}")
    drawing = show_drawing_CRT(cycles)
    print(drawing)


if __name__ == "__main__":
    raise SystemExit(main())
