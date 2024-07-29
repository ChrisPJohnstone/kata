def square_digits(num: int) -> int:
    return int("".join([str(int(n) * int(n)) for n in str(num)]))


if __name__ == "__main__":
    test: int = 9119
    result: int = square_digits(test)
    print(result)
