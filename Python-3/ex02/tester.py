from DiamondTrap import King


def main():
    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)
        return (0)
    except BaseException as err:
        print(f"{err.__class__.__name__}: {err}")
        return (1)


if (__name__ == "__main__"):
    main()
