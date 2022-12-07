import pytest

from day2 import get_total_points


TEST_TXT = """\
A Y
B X
C Z\
"""
EXPECTED_PART_1 = 15
EXPECTED_PART_2 = 12


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_1),),
)
def test_get_total_points_part_1(test_txt: str, expected: int) -> None:
    assert get_total_points(test_txt, 1) == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_2),),
)
def test_get_total_points_part_2(test_txt: str, expected: int) -> None:
    assert get_total_points(test_txt, 2) == expected
