import pytest

from day5 import get_initial_setup, rearrange_crates

TEST_TXT = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2\
"""
EXPECTED_PART_1 = "CMZ"
EXPECTED_PART_2 = "MCD"


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_1),),
)
def test_crates_rearrangement_part1(test_txt: str, expected: int) -> None:
    file = test_txt.split("\n\n")
    n_stacks = int(file[0].split("\n")[-1][-2])
    initial_setup = get_initial_setup(file[0], n_stacks)
    assert rearrange_crates(initial_setup, file[1], 1) == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT, EXPECTED_PART_2),),
)
def test_crates_rearrangement_part2(test_txt: str, expected: int) -> None:
    file = test_txt.split("\n\n")
    n_stacks = int(file[0].split("\n")[-1][-2])
    initial_setup = get_initial_setup(file[0], n_stacks)
    assert rearrange_crates(initial_setup, file[1], 2) == expected
