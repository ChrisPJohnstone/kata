def calc(expression: str) -> int:
    parenthesis_pairs: dict[int, int] = {}
    open_indices: list[int] = []
    for index, character in enumerate(expression):
        if character == "(":
            open_indices.append(index)
        if character == ")":
            parenthesis_pairs[open_indices[-1]] = index
            open_indices.pop(-1)
    print(parenthesis_pairs)


if __name__ == "__main__":
    test: str = "1 + 2 * 5 + ((4 * 2) / 2)"
    result: int = calc(test)
    print(result)
