from abc import ABC, abstractmethod


class Character(ABC):
    """Character interface to use for inheritance."""
    @abstractmethod
    def __init__(self, fn: str, ia: bool = True):
        """Gives a Character his name and life."""
        self.first_name = fn
        self.is_alive = ia

    def die(self):
        """Gives death to a Character"""
        if (self.is_alive):
            self.is_alive = False


class Stark(Character):
    """Character Stark definition."""
    def __init__(self, *args, **kwargs):
        """Gives name and life to Stark character."""
        super().__init__(*args, **kwargs)
