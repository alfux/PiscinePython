from in_out import outer
from in_out import square
from in_out import pow


def main() -> int:
    """Makes some tests bruh."""
    try:
        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())
        return (0)
    except BaseException as err:
        print(f"{err.__class__.__name__}: {err}")


if (__name__ == "__main__"):
    main()
