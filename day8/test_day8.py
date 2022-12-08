from typing import Tuple

import numpy as np
import pytest

from day8 import get_invisible_trees, get_scenic_scores

TEST_TXT = """\
30373
25512
65332
33549
35390\
"""

EXPECTED_INVISIBLE_MAP = np.array(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
)


EXPECTED_SCENIC_SCORES = [4, 8]

EXPECTED_PART_1 = 21
EXPECTED_PART_2 = 8


@pytest.mark.parametrize(
    ("test_txt", "expected_map", "expected"),
    ((TEST_TXT, EXPECTED_INVISIBLE_MAP, EXPECTED_PART_1),),
)
def test_get_invisible_trees(
    test_txt: str, expected_map: np.ndarray, expected: int
) -> None:
    invisible_array = get_invisible_trees(test_txt)
    assert (invisible_array == expected_map).all()
    assert sum(sum(invisible_array == 0)) == expected


@pytest.mark.parametrize(
    ("test_txt", "expected_scenic_scores", "expected"),
    ((TEST_TXT, EXPECTED_SCENIC_SCORES, EXPECTED_PART_2),),
)
def test_get_scenic_scores(
    test_txt: str, expected_scenic_scores: np.ndarray, expected: int
) -> None:
    scenic_scores = get_scenic_scores(test_txt)
    assert scenic_scores[1, 2] == expected_scenic_scores[0]
    assert scenic_scores[3, 2] == expected_scenic_scores[1]
    assert scenic_scores.max() == expected
