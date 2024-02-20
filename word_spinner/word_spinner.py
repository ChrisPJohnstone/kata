def spin_words(sentence: str) -> str:
    words: list[str] = sentence.split(" ")
    output: list[str] = []

    for word in words:
        if len(word) >= 5:
            output.append(word[::-1])
        else:
            output.append(word)
    return " ".join(output)


if __name__ == "__main__":
    test_sentence: str = "Hey fellow warriors"
    result: str = spin_words(test_sentence)
    print(result)
