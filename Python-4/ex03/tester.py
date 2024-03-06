from new_student import Student


def main():
    """Makes some tests bruh."""
    try:
        student = Student(name="Edward", surname="agle")
        print(student)
        student = Student(name="Edward", surname="agle", id="toto")
        print(student)
    except BaseException as err:
        print(f"{err.__class__.__name__}: {err}")


if (__name__ == "__main__"):
    main()
