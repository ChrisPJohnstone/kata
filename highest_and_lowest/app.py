def high_and_low(numbers: str) -> str:
    values: list[int] = [int(n) for n in numbers.split(" ")]
    return f"{max(values)} {min(values)}"


if __name__ == "__main__":
    test: str = "1 2 3 -6 5"
    result: str = high_and_low(test)
    print(result)
