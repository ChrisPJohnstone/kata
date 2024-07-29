def array_diff(a: list[int], b: list[int]) -> list[int]:
    return [n for n in a if n not in b]


if __name__ == "__main__":
    test: list[list[int]] = [
        [1, 2, 2, 2, 3],
        [2],
    ]
    result: list[int] = array_diff(*test)
    print(result)
