from math import floor


def make_readable(seconds: int) -> str:
    output_seconds: int = seconds % 60
    minutes: int = floor(seconds / 60)
    output_minutes: int = minutes % 60
    output_hours: int = floor(minutes / 60)
    return f"{output_hours:02d}:{output_minutes:02d}:{output_seconds:02d}"


if __name__ == "__main__":
    test: int = 121
    result: str = make_readable(test)
    print(result)
