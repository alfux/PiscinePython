from ft_calculator import calculator


def main():
    """Test program."""
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        calculator.dotproduct(a, b)
        calculator.add_vec(a, b)
        calculator.sous_vec(a, b)
        return (0)
    except BaseException as err:
        print(f"{err.__class__.__name__}: {err}")
        return (1)


if (__name__ == "__main__"):
    main()
