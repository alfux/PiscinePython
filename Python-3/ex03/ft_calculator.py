class calculator:
    """Process usual maths operation on objecttors."""
    def __init__(self, vector):
        """Initializes self with the given vecor."""
        if (hasattr(vector, "__iter__")):
            self._vec = vector
        else:
            self._vec = list([vector])

    def __add__(self, object) -> None:
        """Adds object to self."""
        self._vec = [x + object for x in self._vec]
        print(self._vec)

    def __mul__(self, object) -> None:
        """Multiply self with object."""
        self._vec = [x * object for x in self._vec]
        print(self._vec)

    def __sub__(self, object) -> None:
        """Substract object to self."""
        self._vec = [x - object for x in self._vec]
        print(self._vec)

    def __truediv__(self, object) -> None:
        """Divide self by object."""
        try:
            self._vec = [x / object for x in self._vec]
            print(self._vec)
        except BaseException as err:
            print(f"{err.__class__.__name__}: {err}")
