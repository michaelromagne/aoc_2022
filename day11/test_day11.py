import pytest

from day11 import compute_monkey_business

TEST_TXT_SIMPLE = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1\
"""
EXPECTED_PART_1 = 10605
EXPECTED_PART_2 = 2713310158


@pytest.mark.parametrize(
    ("test_txt", "expected", "expected_2"),
    ((TEST_TXT_SIMPLE, EXPECTED_PART_1, EXPECTED_PART_2),),
)
def test_compute_monkey_business(test_txt: str, expected: int, expected_2: int) -> None:

    assert compute_monkey_business(test_txt, 20, 3) == expected
    assert compute_monkey_business(test_txt, 10000, 1) == expected_2
