class calculator:
    """Process operations on two vectors."""
    def __init__(self):
        """Instanciate an empty calculator object.."""
        pass

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Prints dot product of two vectors."""
        new = [x * y for (x, y) in zip(V1, V2)]
        print(f"Dot product is: {sum(new)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Prints sum of two vectors."""
        new = [float(x + y) for (x, y) in zip(V1, V2)]
        print(f"Add Vector is: {new}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Prints difference of two vectors."""
        new = [float(x - y) for (x, y) in zip(V1, V2)]
        print(f"Sous Vector is: {new}")
