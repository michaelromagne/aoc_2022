import pytest

from day6 import get_start_of_packet, get_start_of_message

TEST_TXT_LIST = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]
EXPECTED_PART_1 = [7, 5, 6, 10, 11]
EXPECTED_PART_2 = [19, 23, 23, 29, 26]


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT_LIST, EXPECTED_PART_1),),
)
def test_get_start_of_packet(test_txt: str, expected: int) -> None:
    start_of_paquet_list = [get_start_of_packet(datastream) for datastream in test_txt]
    assert start_of_paquet_list == expected


@pytest.mark.parametrize(
    ("test_txt", "expected"),
    ((TEST_TXT_LIST, EXPECTED_PART_2),),
)
def test_get_start_of_message(test_txt: str, expected: int) -> None:
    start_of_message_list = [
        get_start_of_message(datastream) for datastream in test_txt
    ]
    assert start_of_message_list == expected
