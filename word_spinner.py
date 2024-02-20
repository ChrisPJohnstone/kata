"""
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:
"Hey fellow warriors"  --> "Hey wollef sroirraw"
"This is a test        --> "This is a test"
"This is another test" --> "This is rehtona test"
"""


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
