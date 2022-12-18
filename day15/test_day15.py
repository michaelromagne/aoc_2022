import pytest

from day15 import get_scanned_positions_in_row, get_tuning_frequency

TEST_TXT = """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3\
"""

EXPECTED_PART_1 = 26
EXPECTED_PART_1_BIS = 25
EXPECTED_PART_2 = 56000011


@pytest.mark.parametrize(
    ("test_txt", "expected", "expected_bis"),
    ((TEST_TXT, EXPECTED_PART_1, EXPECTED_PART_1_BIS),),
)
def test_get_scanned_positions(
    test_txt: str,
    expected: int,
    expected_bis: int,
) -> None:
    scanned_positions = get_scanned_positions_in_row(test_txt, 10)
    assert len(scanned_positions) == expected
    assert len(get_scanned_positions_in_row(test_txt, 9)) == expected_bis


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_2),),
)
def test_get_tuning_frequency(
    test_txt: str,
    expected: int,
) -> None:
    tuning_frequency = get_tuning_frequency(test_txt, grid_min=3, grid_max=20)
    assert tuning_frequency == expected
