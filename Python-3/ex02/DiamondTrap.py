from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """What an abomination. Really."""
    def __init__(self, *args, **kwargs):
        """Initializes abominations."""
        super().__init__(*args, **kwargs)

    def get_eyes(self):
        """Eyes getter."""
        return (self.eyes)

    def set_eyes(self, value: str):
        """Eyes setter."""
        self.eyes = value

    def get_hairs(self):
        """Hairs getter."""
        return (self.hairs)

    def set_hairs(self, value: str):
        """Hairs setter."""
        self.hairs = value

    _eyes = property(fget=get_eyes, fset=set_eyes)
    _hairs = property(fget=get_hairs, fset=set_hairs)
