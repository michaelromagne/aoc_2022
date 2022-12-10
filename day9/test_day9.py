import pytest

from day9 import compute_tail_positions

TEST_TXT = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2\
"""

TEST_TXT_2 = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20\
"""

EXPECTED_PART_1 = 13
EXPECTED_PART_2 = 1
EXPECTED_PART_2_BIS = 36


@pytest.mark.parametrize(
    ("test_txt", "expected_1", "expected_2"),
    ((TEST_TXT, EXPECTED_PART_1, EXPECTED_PART_2),),
)
def test_compute_knots_positions(
    test_txt: str, expected_1: int, expected_2: int
) -> None:
    knot_positions_set_2_knots = compute_tail_positions(test_txt, 2)
    assert len(knot_positions_set_2_knots) == expected_1
    knot_positions_set_10_knots = compute_tail_positions(test_txt, 10)
    assert len(knot_positions_set_10_knots) == expected_2


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT_2, EXPECTED_PART_2_BIS),),
)
def test_compute_knots_positions_bis(test_txt: str, expected: int) -> None:
    knot_positions_set_10_knots = compute_tail_positions(test_txt, 10)
    assert len(knot_positions_set_10_knots) == expected
