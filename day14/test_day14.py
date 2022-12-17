import pytest

from day14 import get_sand_position, get_sand_position_part_2

TEST_TXT = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9\
"""

EXPECTED_PART_1 = 24
EXPECTED_PART_2 = 93


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_1),),
)
def test_get_sand_position(
    test_txt: str,
    expected: int,
) -> None:
    sand_position = get_sand_position(test_txt)
    assert len(sand_position) == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_2),),
)
def test_get_sand_position_part_2(
    test_txt: str,
    expected: int,
) -> None:
    sand_position = get_sand_position_part_2(test_txt)
    assert len(sand_position) == expected
