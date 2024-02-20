import re


def get_pig_word(word: str) -> str:
    if not re.match('^[a-zA-Z0-9]+$', word):
        return word
    return f"{word[1:]}{word[0]}ay" 


def pig_it(text: str) -> str:
    return " ".join([get_pig_word(word) for word in text.split(" ")])


if __name__ == "__main__":
    test_text: str = "A series of words"
    result: str = pig_it(test_text)
    print(result)
