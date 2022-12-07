from typing import Tuple

import pytest

from day7 import SIZE_THRESHOLD, get_folder_sizes, get_folder_to_delete, scan_filesystem

TEST_TXT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
dir e
$ cd e
$ ls
2 e
29 z
$ cd ..
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k\
"""

EXPECTED_TREE = {
    "/": {
        "a": {
            "e": {
                "i": 584,
                "e": {
                    "e": 2,
                    "z": 29,
                },
            },
            "f": 29116,
            "g": 2557,
            "h.lst": 62596,
        },
        "b.txt": 14848514,
        "c.dat": 8504156,
        "d": {
            "j": 4060174,
            "d.log": 8033020,
            "d.ext": 5626152,
            "k": 7214296,
        },
    },
}

EXPECTED_SIZES = {
    "/": 48381196,
    "/a": 94884,
    "/d": 24933642,
    "/a/e": 615,
    "/a/e/e": 31,
}
EXPECTED_PART_1 = 95530
EXPECTED_PART_2 = ("/d", 24933642)


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_TREE),),
)
def test_scan_filesystem(test_txt: str, expected: int) -> None:
    filesystem = scan_filesystem(test_txt)
    print(filesystem)
    assert filesystem == expected


@pytest.mark.parametrize(
    ("tree", "expected_sizes", "expected_sum"),
    ((EXPECTED_TREE, EXPECTED_SIZES, EXPECTED_PART_1),),
)
def test_get_folder_sizes(tree: str, expected_sizes: int, expected_sum: int) -> None:
    folder_sizes = get_folder_sizes(tree)
    assert folder_sizes == expected_sizes
    assert (
        sum(
            folder_size
            for folder_size in folder_sizes.values()
            if folder_size <= SIZE_THRESHOLD
        )
        == expected_sum
    )


@pytest.mark.parametrize(
    ("folder_sizes", "expected_folder"),
    ((EXPECTED_SIZES, EXPECTED_PART_2),),
)
def test_get_folder_to_delete(
    folder_sizes: str,
    expected_folder: Tuple[str, int],
) -> None:
    print(get_folder_to_delete)

    assert get_folder_to_delete(folder_sizes) == expected_folder
