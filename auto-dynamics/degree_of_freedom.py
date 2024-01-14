"""A class to handle a single simple degree of freedom."""
from uuid import uuid4


class GeneralizedCoordinate:
    """A class for a single degree of freedom."""

    def __init__(self, val: float = 0):
        """Initiazize self with the given vales."""
        self.val = val

    def __iadd__(self, val: float):
        """Update the values in self."""
        self.val = val


class GeneralizedVelocity:
    """A class for a single degree of freedom."""

    def __init__(self, val: float = 0):
        """Initiazize self with the given vales."""
        self.val = val

    def __iadd__(self, val: float):
        """Update the values in self."""
        self.val = val


class DegreeOfFreedom:
    """Initialize a coordinate, velocity pair."""

    def __init__(self, label: str = None, q: float = 0, q_dot: float = 0):
        """Initialze both the coordinate and veolicty."""
        if label is None:
            self.label = uuid4()
        self.q = GeneralizedCoordinate(q)
        self.p = GeneralizedVelocity(q_dot)
