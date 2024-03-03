from S1E9 import Character


class Baratheon(Character):
    """The Baratheon family."""
    def __init__(self, *args, **kwargs):
        """Gives name and life to Baratheon member."""
        super().__init__(*args, **kwargs)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Returns informal string representation."""
        return (f"('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """Returns official string representation."""
        return (f"Vector: {self}")


class Lannister(Character):
    """The Lannister family."""
    def __init__(self, *args, **kwargs):
        """Gives name anf life to Lannister member."""
        super().__init__(*args, **kwargs)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Returns informal string representation."""
        return (f"('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """Returns official string representation."""
        return (f"Vector: {self}")

    @classmethod
    def create_lannister(self, *args, **kwargs):
        """Create a new Lannister."""
        return (Lannister(*args, **kwargs))
