from enum import Enum


class Color(Enum):
    """ANSI color codes"""
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    grey = 37
    white = 38


def cprint(color_code: Color, *args, **kwargs) -> None:
    """
    Prints colored text

    :param color_code: Color Enum
    :return: None
    """
    args = [f"\033[{color_code.value}m{string}\033[00m" for string in args]
    print(*args, **kwargs)


if __name__ == "__main__":
    for color in Color:
        cprint(color, color.name)
