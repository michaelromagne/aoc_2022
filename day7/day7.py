"""Advent of code 2022 - Day 7"""

import operator
import os
import sys
from functools import reduce  # forward compatibility for Python 3
from typing import Dict, List, Tuple, Union

from typing_extensions import TypeAlias

sys.setrecursionlimit(10000)

NestedDict: TypeAlias = Dict[str, Union[int, "NestedDict"]]

INPUT_TXT = os.path.join(os.path.dirname(__file__), "terminal_output.txt")

CD_COMMAND = "$ cd "
GO_BACK = ".."
DIR = "dir"
SIZE_THRESHOLD = 100000
DISK_SPACE = 70000000
NEEDED_SPACE = 30000000
ROOT_PATH = "/"


def get_from_dict(file_system: NestedDict, current_path: List[str]):
    return reduce(operator.getitem, current_path, file_system)


def set_in_dict(file_system: NestedDict, current_path: List[str], content: NestedDict):
    get_from_dict(file_system, current_path[:-1])[current_path[-1]] = content


def sum_values_dict(nested_dict: NestedDict):
    sum = 0
    for v in nested_dict.values():
        if isinstance(v, dict):
            sum += sum_values_dict(v)
        else:
            sum += v
    return sum


def scan_filesystem(terminal_output: str) -> NestedDict:
    """Return a dictionary representing the filesystem."""
    # Parse terminal output
    parsed_terminal_output = terminal_output.split(CD_COMMAND)[1:]
    command_list = [
        list(filter(None, command.split("\n"))) for command in parsed_terminal_output
    ]
    # Scan folders
    file_system = {}
    current_path = []
    for command in command_list:
        if command[0] == GO_BACK:
            current_path = current_path[:-1]
        else:
            current_path += [command[0]]
            split_content = [content.split(" ") for content in command[2:]]
            content_sizes = {
                content[1]: {} if content[0] == DIR else int(content[0])
                for content in split_content
            }
            set_in_dict(file_system, current_path, content_sizes)
    return file_system


def get_folder_sizes(
    file_system: NestedDict,
    folder_sizes={},
    initial_path="",
) -> Dict[str, int]:
    for k, v in file_system.items():
        if isinstance(v, dict):
            if k == ROOT_PATH:
                current_path = k
            elif initial_path == ROOT_PATH:
                current_path = "".join([initial_path, k])
            else:
                current_path = ROOT_PATH.join([initial_path, k])
            folder_sizes[current_path] = sum_values_dict(file_system[k])

            get_folder_sizes(v, folder_sizes, current_path)
    return folder_sizes


def get_folder_to_delete(folder_sizes: Dict[str, int]) -> Tuple[str, int]:
    current_left_space = DISK_SPACE - folder_sizes[ROOT_PATH]
    min_space_to_free = NEEDED_SPACE - current_left_space
    lowest_size = min([v for v in folder_sizes.values() if v > min_space_to_free])
    folder_to_delete = [
        folder_path for folder_path, size in folder_sizes.items() if size == lowest_size
    ][0]
    return folder_to_delete, lowest_size


def main():
    with open(INPUT_TXT) as f:
        terminal_output = f.read()
    file_system = scan_filesystem(terminal_output)
    folder_sizes = get_folder_sizes(file_system)
    print(
        f"""Sum of light folders sizes: {
        sum(folder_size
        for folder_size in folder_sizes.values()
        if folder_size <= SIZE_THRESHOLD
    )
    }"""
    )
    folder_to_delete, size_folder_to_delete = get_folder_to_delete(folder_sizes)
    print(f"Folder to delete is {folder_to_delete}, size {size_folder_to_delete}")


if __name__ == "__main__":
    raise SystemExit(main())
