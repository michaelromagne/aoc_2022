import pytest

from day10 import compute_X, show_drawing_CRT

TEST_TXT_SIMPLE = """\
noop
addx 3
addx -5\
"""

TEST_TXT = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop\
"""

EXPECTED_CYCLES = [1, 1, 1, 4, 4, -1]
EXPECTED_PART_1 = 13140

EXPECTED_DRAWING = """\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....\
"""

EXPECTED_PART_2 = 36


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT_SIMPLE, EXPECTED_CYCLES),),
)
def test_compute_X__simple(test_txt: str, expected: list) -> None:
    X = compute_X(test_txt)
    assert X == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_1),),
)
def test_compute_X(test_txt: str, expected: list) -> None:
    X = compute_X(test_txt)
    assert (
        X[19] * 20
        + X[59] * 60
        + X[99] * 100
        + X[139] * 140
        + X[179] * 180
        + X[219] * 220
        == expected
    )


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_DRAWING),),
)
def test_show_drawing_CRT(test_txt: str, expected: list) -> None:
    pixels = show_drawing_CRT(test_txt)
    print(pixels)
    assert pixels == expected
