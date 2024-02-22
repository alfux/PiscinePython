import sys as sys


def convert_to_morse(text: str) -> str:
    """Returns a list of converted characters into Morse code."""
    code = {' ': "/", 'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..",
            'E': ".", 'F': "..-.", 'G': "--.", 'H': "....", 'I': "..",
            'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.",
            'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...",
            'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
            'Y': "-.--", 'Z': "--..", '1': ".----", '2': "..---", '3': "...--",
            '4': "....-", '5': ".....", '6': "-....", '7': "--...",
            '8': "---..", '9': "----.", '0': "-----"}
    try:
        return [code[c.upper()] for c in text]
    except BaseException:
        raise AssertionError("the arguments are bad")


def main(av: list) -> int:
    """Prints a string into Morse code, returns 0 on success, 1 otherwise."""
    try:
        if (len(av) != 2):
            raise AssertionError("the arguments are bad")
        print(*convert_to_morse(av[1]))
    except BaseException as err:
        print(err.__class__.__name__ + ':', err, file=sys.stderr)
        return (1)
    return (0)


if __name__ == "__main__":
    main(sys.argv)
