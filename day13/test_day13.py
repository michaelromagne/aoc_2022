from typing import List

import pytest

from day13 import get_right_order_indices, sort_packets

TEST_TXT = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]\
"""
EXPECTED_RIGHT_ORDER_LIST = [1, 2, 4, 6]
EXPECTED_PART_1 = 13

EXPECTED_PART_2 = 140


@pytest.mark.parametrize(
    ("test_txt", "expected_order", "expected"),
    ((TEST_TXT, EXPECTED_RIGHT_ORDER_LIST, EXPECTED_PART_1),),
)
def test_get_right_order_indices(
    test_txt: str,
    expected_order: List[int],
    expected: int,
) -> None:
    right_order_indices = get_right_order_indices(test_txt)
    indices_true = [
        index + 1 for index, item in enumerate(right_order_indices) if item == 1
    ]
    assert indices_true == expected_order
    assert sum(indices_true) == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_2),),
)
def test_sort_packets(
    test_txt: str,
    expected: str,
) -> None:
    product_indices = sort_packets(test_txt)

    assert product_indices == expected
