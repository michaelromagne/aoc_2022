"""Test day1."""
import pytest

from day1 import get_strongest_elves_calories


TEST_TXT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000\
"""
EXPECTED_PART_1 = 24000
EXPECTED_PART_2 = 45000


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_1),),
)
def test_get_strongest_elves_calories_part1(test_txt: str, expected: int) -> None:
    assert get_strongest_elves_calories(test_txt, 1) == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_2),),
)
def test_get_strongest_elves_calories_part2(test_txt: str, expected: int) -> None:
    assert get_strongest_elves_calories(test_txt, 3) == expected
