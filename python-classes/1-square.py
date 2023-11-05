"""
A class representing a square.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.

        Returns:
            None.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
