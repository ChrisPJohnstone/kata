def find_it(seq: list[int]) -> int:
    values: dict[int, int] = {}
    for value in seq:
        if value not in values:
            values[value] = 0
        values[value] += 1
    return [key for key, value in values.items() if value % 2 == 1][0]


if __name__ == "__main__":
    test_sequence: list[int] = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
    result: int = find_it(test_sequence)
    print(result)
