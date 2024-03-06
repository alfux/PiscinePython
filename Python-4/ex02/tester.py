from callLimit import callLimit


def main() -> int:
    """Makes some tests bruh."""
    try:

        @callLimit(3)
        def f():
            print("f()")

        @callLimit(1)
        def g():
            print("g()")

        for i in range(3):
            f()
            g()
    except BaseException as err:
        print(f"{err.__class__.__name__}: {err}")


if (__name__ == "__main__"):
    main()
