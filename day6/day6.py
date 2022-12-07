"""Advent of code 2022 - Day 7"""

import os
import sys

sys.setrecursionlimit(10000)
INPUT_TXT = os.path.join(os.path.dirname(__file__), "datastream.txt")


def get_start_of_packet(datastream: str, idx: int = 4) -> int:
    """Return the index where the first start-of-packet marker is detected."""
    if len(set(datastream[idx - 4 : idx])) == 4:
        return idx
    else:
        idx += 1
        return get_start_of_packet(datastream, idx)


def get_start_of_message(datastream: str, idx: int = 14) -> int:
    """Return the index where the first start-of-packet marker is detected."""
    if len(set(datastream[idx - 14 : idx])) == 14:
        return idx
    else:
        idx += 1
        return get_start_of_message(datastream, idx)


def main():
    with open(INPUT_TXT) as f:
        file = f.read()
    print(f"Start of packet: {get_start_of_packet(file)}")
    print(f"Start of message: {get_start_of_message(file)}")


if __name__ == "__main__":
    raise SystemExit(main())
