import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random fifteen lowercase letters id."""
    return ("".join(random.choices(string.ascii_lowercase, k=15)))


@dataclass
class Student:
    """Creates a student profile for School's intra."""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Initializes self.login according to self.name and self.surname."""
        if (not len(self.name)):
            raise ValueError("argument <name> can't be empty string")
        if (not len(self.surname)):
            raise ValueError("argument <surname> can't be empty string")
        self.login = self.name[0] + self.surname
