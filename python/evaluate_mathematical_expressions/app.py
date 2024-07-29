def calc(expression: str) -> int:
    # TODO: Handle parenthesis
    #     parenthesis_pairs: dict[int, int] = {}
    #     open_indices: list[int] = []
    #     for index, character in enumerate(expression):
    #         if character == "(":
    #             open_indices.append(index)
    #         if character == ")":
    #             parenthesis_pairs[open_indices[-1]] = index
    #             open_indices.pop(-1)

    clean_expression: str = get_clean_expression(expression)
    outcome: str = evaluate_segment(clean_expression)
    return outcome


def get_clean_expression(expression: str) -> str:
    without_spaces: str = expression.replace(" ", "")
    return without_spaces
    # TODO: Handle double negatives


def evaluate_segment(expression: str) -> str:
    operators: list[str] = ["*", "/", "+", "-"]
    operator_found: str = None
    for operator in operators:
        if operator not in expression:
            continue
        operator_position: int = expression.find(operator)
        operator_found: str = operator

        expression_before: str = expression[:operator_position]
        previous_operator_position: int = 0
        for index, character in enumerate(expression_before[::-1]):
            if character in operators:
                previous_operator_position += len(expression_before) - index
                break
        first_value: int = int(expression_before[previous_operator_position:])

        expression_after: str = expression[operator_position + 1 :]
        next_operator_position: int = 0
        for index, character in enumerate(expression_after):
            if character in operators:
                next_operator_position += index
                break
        if next_operator_position == 0:
            second_value: int = int(expression_after)
        else:
            second_value: int = int(expression_after[:next_operator_position])
        break

    if operator_found is None:
        return expression

    if operator_found == "*":
        outcome: int = first_value * second_value
    elif operator_found == "/":
        outcome: int = int(first_value / second_value)
    elif operator_found == "+":
        outcome: int = first_value + second_value
    elif operator_found == "-":
        outcome: int = first_value - second_value

    constructor: list[str] = [
        expression[:previous_operator_position],
        str(outcome),
    ]
    if next_operator_position:
        constructor.append(expression_after[next_operator_position:])
    new_expression: str = "".join(constructor)
    try:
        int(new_expression)
        return new_expression
    except ValueError:
        return evaluate_segment(new_expression)


if __name__ == "__main__":
    test: str = "1 + 2 * 5 + ((4 * 2) / 2)"
    test: str = "1 - 1 + 30 / 2 + 10"
    result: int = calc(test)
    print(result)
