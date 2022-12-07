import pytest

from day3 import (
    sum_misplaced_objects_priorities,
    sum_group_badges_priorities,
    OBJECTS_PRIORITIES,
)


TEST_TXT = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw\
"""
EXPECTED_PART_1 = 157
EXPECTED_PART_2 = 70


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_1),),
)
def test_sum_misplaced_objects_priorities(test_txt: str, expected: int) -> None:
    assert sum_misplaced_objects_priorities(test_txt, OBJECTS_PRIORITIES) == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_2),),
)
def test_sum_group_badges_priorities(test_txt: str, expected: int) -> None:
    assert sum_group_badges_priorities(test_txt, OBJECTS_PRIORITIES) == expected
