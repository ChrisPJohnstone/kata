def create_phone_number(n: list[int]) -> str:
    phone_number: str = "".join([str(x) for x in n])
    return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"

if __name__ == "__main__":
    test: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    result: str = create_phone_number(test)
    print(result)
