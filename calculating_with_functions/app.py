from typing import Callable


def plus(value: Callable) -> Callable:
    return lambda x: x + value


def minus(value: Callable) -> Callable:
    return lambda x: x - value


def times(value: Callable) -> Callable:
    return lambda x: x * value


def divided_by(value: Callable) -> Callable:
    return lambda x: int(x / value)


def zero(operation: Callable = None, value: int = None) -> int:
    value: int = 0
    return operation(value) if operation else value


def one(operation: Callable = None, value: int = None) -> int:
    value: int = 1
    return operation(value) if operation else value


def two(operation: Callable = None, value: int = None) -> int:
    value: int = 2
    return operation(value) if operation else value


def three(operation: Callable = None, value: int = None) -> int:
    value: int = 3
    return operation(value) if operation else value


def four(operation: Callable = None, value: int = None) -> int:
    value: int = 4
    return operation(value) if operation else value


def five(operation: Callable = None, value: int = None) -> int:
    value: int = 5
    return operation(value) if operation else value


def six(operation: Callable = None, value: int = None) -> int:
    value: int = 6
    return operation(value) if operation else value


def seven(operation: Callable = None, value: int = None) -> int:
    value: int = 7
    return operation(value) if operation else value


def eight(operation: Callable = None, value: int = None) -> int:
    value: int = 8
    return operation(value) if operation else value


def nine(operation: Callable = None, value: int = None) -> int:
    value: int = 9
    return operation(value) if operation else value


if __name__ == "__main__":
    test: int = eight(divided_by(three()))
    print(test)
