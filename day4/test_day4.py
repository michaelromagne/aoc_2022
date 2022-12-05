"""Test day4."""

import pytest

from day4 import count_assignement_fully_contained, count_assignement_overlap


TEST_TXT = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8\
"""
EXPECTED_PART_1 = 2
EXPECTED_PART_2 = 4


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_1),),
)
def test_count_assignement_fully_contained(test_txt: str, expected: int) -> None:
    assert count_assignement_fully_contained(test_txt) == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_2),),
)
def test_count_assignement_overlap(test_txt: str, expected: int) -> None:
    assert count_assignement_overlap(test_txt) == expected
