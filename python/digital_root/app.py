def digital_root(n: int) -> int:
    output: int = n
    while output > 9:
        output: list[int] = sum([int(n) for n in str(output)])
    return output


if __name__ == "__main__":
    test: int = 132189
    result: int = digital_root(test)
    print(result)
