"""Advent of code 2022 - Day 7"""

import os

import numpy as np

INPUT_TXT = os.path.join(os.path.dirname(__file__), "forest.txt")


def get_invisible_trees(forest: str):
    forest_list = forest.splitlines()
    forest_array = np.array(
        [np.array([int(tree) for tree in tree_row]) for tree_row in forest_list]
    )
    invisible_array = np.zeros(forest_array.shape, dtype=int)
    for i in range(1, forest_array.shape[0] - 1):
        for j in range(1, forest_array.shape[1] - 1):
            if (
                (forest_array[i, j] <= max(forest_array[i, :j]))
                & (forest_array[i, j] <= max(forest_array[i, j + 1 :]))
                & (forest_array[i, j] <= max(forest_array[:i, j]))
                & (forest_array[i, j] <= max(forest_array[i + 1 :, j]))
            ):
                invisible_array[i, j] = 1
    return invisible_array


def get_scenic_scores(forest: str):
    forest_list = forest.splitlines()
    forest_array = np.array(
        [np.array([int(tree) for tree in tree_row]) for tree_row in forest_list]
    )
    scenic_scores_array = np.zeros(forest_array.shape, dtype=int)
    for i in range(1, forest_array.shape[0] - 1):
        for j in range(1, forest_array.shape[1] - 1):
            tree_height = forest_array[i, j]
            view_up = (
                i
                - np.concatenate(
                    ([0], np.where(forest_array[:i, j] >= tree_height)[0])
                )[-1]
            )
            view_left = (
                j
                - np.concatenate(
                    ([0], np.where(forest_array[i, :j] >= tree_height)[0])
                )[-1]
            )
            view_right = np.concatenate(
                (
                    np.where(forest_array[i, j + 1 :] >= tree_height)[0] + 1,
                    [forest_array.shape[1] - j - 1],
                )
            )[0]
            view_down = np.concatenate(
                (
                    np.where(forest_array[i + 1 :, j] >= tree_height)[0] + 1,
                    [forest_array.shape[0] - i - 1],
                )
            )[0]
            scenic_scores_array[i, j] = view_up * view_left * view_right * view_down
    return scenic_scores_array


def main():
    with open(INPUT_TXT) as f:
        forest = f.read()
    invisible_array = get_invisible_trees(forest)
    print(f"Sum of visible trees: {sum(sum(invisible_array==0))}")
    scenic_scores_array = get_scenic_scores(forest)
    print(f"Highest scenic score: {scenic_scores_array.max()}")


if __name__ == "__main__":
    raise SystemExit(main())
