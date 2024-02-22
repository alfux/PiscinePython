import sys as sys


def count_characters(text: str):
    """Displays different counters of characters from a string"""
    counter = [0, 0, 0, 0, 0]

    for c in text:
        if (c.isupper()):
            counter[0] += 1
        elif (c.islower()):
            counter[1] += 1
        elif (c.isdigit()):
            counter[2] += 1
        elif (c.isspace()):
            counter[3] += 1
        elif (c.isascii() and c.isprintable()):
            counter[4] += 1
    print("The text contains", len(text), "characters:\n",
          counter[0], "upper letters\n",
          counter[1], "lower letters\n",
          counter[4], "punctuation marks\n",
          counter[3], "spaces\n",
          counter[2], "digits")


def main(av: list):
    """A character counter program's main function"""
    try:
        if (len(av) < 2):
            count_characters(input("What is the text to count?\n"))
        elif (len(av) == 2):
            count_characters(av[1])
        else:
            raise AssertionError("too many arguments")
    except BaseException as err:
        print(err.__class__.__name__ + ':', err)


if __name__ == "__main__":
    main(sys.argv)
