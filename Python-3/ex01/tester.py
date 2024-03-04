from S1E7 import Baratheon, Lannister


def main():
    """Test program."""
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(f"Name : {Jaine.first_name, type(Jaine).__name__}", end='')
        print(f", Alive : {Jaine.is_alive}")
        return (0)
    except BaseException as err:
        print(f"{err.__class__.__name__}: {err}")
        return (1)


if (__name__ == "__main__"):
    main()
