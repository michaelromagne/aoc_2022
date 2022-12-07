"""Advent of code 2022 - Day 4"""
import os

INPUT_DAY4 = os.path.join(os.path.dirname(__file__), "cleaning_pairs.txt")


def count_assignement_fully_contained(cleaning_pairs: str):
    cleaning_pairs_string_list = [
        tuple(pair.split(",")) for pair in cleaning_pairs.split("\n")
    ]
    cleaning_pairs_list = [
        (left.split("-"), right.split("-"))
        for left, right in cleaning_pairs_string_list
    ]
    number_fully_contained = 0
    for left, right in cleaning_pairs_list:
        if int(left[0]) <= int(right[0]) <= int(right[1]) <= int(left[1]):
            number_fully_contained += 1
        elif int(right[0]) <= int(left[0]) <= int(left[1]) <= int(right[1]):
            number_fully_contained += 1

    return number_fully_contained


def count_assignement_overlap(cleaning_pairs: str):
    cleaning_pairs_string_list = [
        tuple(pair.split(",")) for pair in cleaning_pairs.split("\n")
    ]
    cleaning_pairs_list = [
        (left.split("-"), right.split("-"))
        for left, right in cleaning_pairs_string_list
    ]
    number_overlap = 0
    for left, right in cleaning_pairs_list:

        if int(left[0]) <= int(right[0]) <= int(left[1]):
            number_overlap += 1
        elif int(left[0]) <= int(right[1]) <= int(left[1]):
            number_overlap += 1
        elif int(right[0]) <= int(left[1]) <= int(right[1]):
            number_overlap += 1
        elif int(right[0]) <= int(left[0]) <= int(right[1]):
            number_overlap += 1

    return number_overlap


def main():
    with open(INPUT_DAY4, "r") as cleaning_pairs:
        cleaning_pairs = cleaning_pairs.read()
    print(
        f"{count_assignement_fully_contained(cleaning_pairs)} pairs have an assignement that fully contains the other !"
    )
    print(
        f"{count_assignement_overlap(cleaning_pairs)} pairs have overlapping assignements !"
    )


if __name__ == "__main__":
    raise SystemExit(main())
