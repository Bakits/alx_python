"""Square Representing a square object which extended from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing a square object.

    Attributes:
        size (int): Size of the square.
        x (int): X-coordinate position of the square.
        y (int): Y-coordinate position of the square.
        id (int): ID of the square object.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Constructor method to initialize the square.
        __str__(self): Return a string representation of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square object.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate position of the square. Defaults to 0.
            y (int, optional): Y-coordinate position of the square. Defaults to 0.
            id (int, optional): ID of the square object. Defaults to None.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
