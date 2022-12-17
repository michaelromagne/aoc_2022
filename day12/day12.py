"""Advent of code 2022 - Day 12"""
import os

from typing import List, Tuple

import networkx as nx
import numpy as np
from string import ascii_lowercase

INPUT_TXT = os.path.join(os.path.dirname(__file__), "heightmap.txt")

LETTERS_HEIGHT_MAPPING = {}
LETTERS_HEIGHT_MAPPING.update({letter: id for id, letter in enumerate(ascii_lowercase)})


def compute_path(heightmap: str) -> List[Tuple[str, str]]:
    heightmap_list = heightmap.splitlines()
    heightmap_array = np.array(
        [np.array(list(height_row)) for height_row in heightmap_list]
    )
    # Get start and end positions
    begin_position = np.where(heightmap_array == "S")
    heightmap_array[begin_position] = "a"
    begin_position = begin_position[0][0], begin_position[1][0]
    end_position = np.where(heightmap_array == "E")
    heightmap_array[end_position] = "z"
    end_position = end_position[0][0], end_position[1][0]
    # Create graph
    G = nx.DiGraph()

    for i in range(heightmap_array.shape[0]):
        for j in range(heightmap_array.shape[1]):
            G.add_node((i, j))

            if i < heightmap_array.shape[0] - 1:
                if (
                    LETTERS_HEIGHT_MAPPING[heightmap_array[i, j]]
                    >= LETTERS_HEIGHT_MAPPING[heightmap_array[i + 1, j]] - 1
                ):
                    G.add_edge((i, j), (i + 1, j))

            if i > 0:
                if (
                    LETTERS_HEIGHT_MAPPING[heightmap_array[i, j]]
                    >= LETTERS_HEIGHT_MAPPING[heightmap_array[i - 1, j]] - 1
                ):
                    G.add_edge((i, j), (i - 1, j))

            if j < heightmap_array.shape[1] - 1:
                if (
                    LETTERS_HEIGHT_MAPPING[heightmap_array[i, j]]
                    >= LETTERS_HEIGHT_MAPPING[heightmap_array[i, j + 1]] - 1
                ):
                    G.add_edge((i, j), (i, j + 1))

            if j > 0:
                if (
                    LETTERS_HEIGHT_MAPPING[heightmap_array[i, j]]
                    >= LETTERS_HEIGHT_MAPPING[heightmap_array[i, j - 1]] - 1
                ):
                    G.add_edge((i, j), (i, j - 1))
    path = nx.shortest_path(G, begin_position, end_position)
    return path


def compute_path_part_2(heightmap: str) -> List[Tuple[str, str]]:

    heightmap_list = heightmap.splitlines()
    heightmap_array = np.array(
        [np.array(list(height_row)) for height_row in heightmap_list]
    )
    # Get start and end positions
    begin_position = np.where(heightmap_array == "S")
    heightmap_array[begin_position] = "a"

    possible_begin_positions = np.where(heightmap_array == "a")

    end_position = np.where(heightmap_array == "E")
    heightmap_array[end_position] = "z"
    end_position = end_position[0][0], end_position[1][0]
    # Create graph
    G = nx.DiGraph()
    for i in range(heightmap_array.shape[0]):
        for j in range(heightmap_array.shape[1]):
            G.add_node((i, j))

            if i < heightmap_array.shape[0] - 1:
                if (
                    LETTERS_HEIGHT_MAPPING[heightmap_array[i, j]]
                    >= LETTERS_HEIGHT_MAPPING[heightmap_array[i + 1, j]] - 1
                ):
                    G.add_edge((i, j), (i + 1, j))

            if i > 0:
                if (
                    LETTERS_HEIGHT_MAPPING[heightmap_array[i, j]]
                    >= LETTERS_HEIGHT_MAPPING[heightmap_array[i - 1, j]] - 1
                ):
                    G.add_edge((i, j), (i - 1, j))

            if j < heightmap_array.shape[1] - 1:
                if (
                    LETTERS_HEIGHT_MAPPING[heightmap_array[i, j]]
                    >= LETTERS_HEIGHT_MAPPING[heightmap_array[i, j + 1]] - 1
                ):
                    G.add_edge((i, j), (i, j + 1))

            if j > 0:
                if (
                    LETTERS_HEIGHT_MAPPING[heightmap_array[i, j]]
                    >= LETTERS_HEIGHT_MAPPING[heightmap_array[i, j - 1]] - 1
                ):
                    G.add_edge((i, j), (i, j - 1))
    paths = []
    for begin_position in list(
        zip(possible_begin_positions[0], possible_begin_positions[1])
    ):
        try:
            path = nx.shortest_path(G, begin_position, end_position)
            paths.append(path)
        except:
            print("No path !")

    return min(paths, key=len)


def main():
    with open(INPUT_TXT) as f:
        heightmap = f.read()
    path = compute_path(heightmap)
    print(f"Number of steps to climb hill: {len(path)-1}")
    path_part_2 = compute_path_part_2(heightmap)
    print(f"Number of steps to climb hill part 2: {len(path_part_2)-1}")


if __name__ == "__main__":
    raise SystemExit(main())
