"""Advent of code 2022 - Day 1"""


INPUT_DAY1 = "elves_food.txt"


def get_strongest_elves_calories(
    elves_food: str,
    n_elves: int,
):
    """Get calories carried by the n strongest elves."""
    food_string_list = [food.split("\n") for food in elves_food.split("\n\n")]
    # Prepend "0" to food string to avoid exception when a blank line is at the end of the file
    food_list = [
        [int("0" + food) for food in food_list] for food_list in food_string_list
    ]

    if n_elves < 1:
        raise ValueError("You should have n_elves greater than 1 !")
    sum_food_per_elve = [sum(food_elve) for food_elve in food_list]
    sorted_sum_food = sorted(sum_food_per_elve)
    return sum(sorted_sum_food[-n_elves:])


def main():
    with open(INPUT_DAY1, "r") as elves_food:
        elves_food = elves_food.read()
    print(
        f"Total calories for the strongest elve : {get_strongest_elves_calories(elves_food, 1)}"
    )
    print(
        f"Total calories for the 3 strongest elves : {get_strongest_elves_calories(elves_food, 3)}"
    )


if __name__ == "__main__":
    raise SystemExit(main())
