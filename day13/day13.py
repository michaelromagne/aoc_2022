"""Advent of code 2022 - Day 13"""
import ast
import functools
import os
from typing import List, Union
import numpy as np

INPUT_TXT = os.path.join(os.path.dirname(__file__), "distress_signal.txt")


def product(s):
    if s:
        return functools.reduce(lambda x, y: x * y, s)


def check_order(
    left: Union[int, List[int]],
    right: Union[int, List[int]],
) -> int:
    if isinstance(left, int):
        if isinstance(right, int):
            return np.sign(right - left)
        else:
            return check_order([left], right)
    if isinstance(right, int):
        return check_order(left, [right])
    for left_element, right_element in list(zip(left, right)):
        order = check_order(left_element, right_element)
        if (order != 0) & (order is not None):
            return order
    if len(left) != len(right):
        return np.sign(len(right) - len(left))


def get_right_order_indices(distress_signal_packets: str) -> List[int]:
    packets_pairs_list = [
        packets.split("\n") for packets in distress_signal_packets.split("\n\n")
    ]
    # Converting string to list
    packets_pairs_list = [
        (ast.literal_eval(pair[0]), ast.literal_eval(pair[1]))
        for pair in packets_pairs_list
    ]
    # Compare pairs
    pair_comparison = []
    for pair in packets_pairs_list:
        comparison = check_order(pair[0], pair[1])
        pair_comparison.append(comparison)
    return pair_comparison


def sort_packets(distress_signal_packets: str) -> int:
    packets_list = []
    packets_split = distress_signal_packets.split("\n\n")
    for packets in packets_split:
        packets_list += packets.split("\n")
    target_packets = [[[2]], [[6]]]
    target_indices = []
    for target_packet in target_packets:
        i = 1
        for packet in packets_list:
            if check_order(eval(packet), target_packet) == 1:
                i += 1
        for packet in target_packets:
            if target_packet != packet:
                if check_order(packet, target_packet) == 1:
                    i += 1
        target_indices.append(i)

    return product(target_indices)


def main():
    with open(INPUT_TXT) as f:
        distress_signal_packets = f.read()
    right_order_indices = get_right_order_indices(distress_signal_packets)
    indices_true = [
        index + 1 for index, item in enumerate(right_order_indices) if item == 1
    ]
    print(f"Sum of indices with right order : {sum(indices_true)}")
    print(
        f"Product of indices for target packets: {sort_packets(distress_signal_packets)}"
    )


if __name__ == "__main__":
    raise SystemExit(main())
