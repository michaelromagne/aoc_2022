"""Advent of code 2022 - Day 7"""

import os
import sys

sys.setrecursionlimit(10000)
INPUT_TXT = os.path.join(os.path.dirname(__file__), "datastream.txt")


def get_start_of_block(
    datastream: str,
    idx: int = 4,
    block_size: int = 4,
) -> int:
    """Return the index where the first start-of-packet marker is detected."""
    if len(set(datastream[idx - block_size : idx])) == block_size:
        return idx
    else:
        idx += 1
        return get_start_of_block(datastream, idx, block_size)


def main():
    with open(INPUT_TXT) as f:
        file = f.read()
    print(f"Start of packet: {get_start_of_block(datastream=file, block_size=4)}")
    print(f"Start of message: {get_start_of_block(datastream=file, block_size=14)}")


if __name__ == "__main__":
    raise SystemExit(main())
