def get_factors(n: int) -> list[int]:
    return [factor for factor in range(3, n) if n % factor == 0]


def get_prime_factors(n: int) -> list[int]:
    factors: list[int] = get_factors(n)
    return [factor for factor in factors if get_factors(factor) == []]


if __name__ == "__main__":
    test_number: int = 15
    result: list[int] = get_prime_factors(test_number)
    print(result)

