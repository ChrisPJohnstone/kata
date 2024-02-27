def descending_order(num: int) -> int:
    numbers: list[int] = [n for n in str(num)]
    numbers.sort(reverse=True)
    return int("".join(numbers))


if __name__ == "__main__":
    test: int = 42145
    result: int = descending_order(test)
    print(result)
