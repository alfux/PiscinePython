def square(x: int | float) -> int | float:
    """Returns square of <x>."""
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """Returns <x> to the power of <x>."""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """Creates an iterative composition of <function> evaluated in <x>."""

    def inner() -> float:
        """Returns <function> composed with itself * count evaluated in <x>."""
        nonlocal x
        x = function(x)
        return (x)

    return (inner)
