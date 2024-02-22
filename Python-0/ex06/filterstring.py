import sys as sys
from ft_filter import ft_filter


def main(av: list) -> int:
    """main(av: list) -> int

Program that accepts two arguments: a string(S), and an integer(N). The program
outputs a list of words from S that have a length greater than N"""
    try:
        if (len(av) != 3):
            raise AssertionError("the arguments are bad")
        try:
            print(ft_filter(lambda x: len(x) > int(av[2]),
                  [e for e in av[1].split()]))
        except BaseException:
            raise AssertionError("the arguments are bad")
    except BaseException as err:
        print(err.__class__.__name__ + ':', err, file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv)
