from statistics import ft_statistics


def main() -> int:
    try:
        ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                      tata="quartile")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std",
                      world="var")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                      ejdjdejn="kdekem")
        print("-----")
        ft_statistics(toto="mean", tutu="median", tata="quartile")
        return (0)
    except BaseException as err:
        print(f"{err.__class__.__name__}: {err}")
        return (1)


if (__name__ == "__main__"):
    main()
