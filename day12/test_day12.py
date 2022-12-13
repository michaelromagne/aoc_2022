import pytest

from day12 import compute_path, compute_path_part_2

TEST_TXT = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi\
"""
EXPECTED_PART_1 = 31
EXPECTED_PART_2 = 29


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_1),),
)
def test_compute_path(test_txt: str, expected: int) -> None:
    path = compute_path(test_txt)
    assert len(path) - 1 == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_2),),
)
def test_compute_path_part_2(test_txt: str, expected: int) -> None:
    path = compute_path_part_2(test_txt)
    assert len(path) - 1 == expected
