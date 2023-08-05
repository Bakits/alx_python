#!/usr/bin/python3
"""A class representing a rectangle, inheriting from Rectangle."""
Rectangle = __import__("7-rectangle").Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    This class inherits from the Rectangle class and provides functionality to represent a square.
    It includes validation for a positive integer value for the size of the square.

    Attributes:
        __size (int): The size of the square (private attribute).

    Methods:
        __init__(self, size):
            Initializes a new Square object with the given size.

        area(self):
            Calculate the area of the square.

        __str__(self):
            Returns a string representation of the Square in the format [Square] size/size.

    """

    def __init__(self, size):
        """
        Initializes a new Square object with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is not a positive integer.

        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square in the format [Square] size/size.

        Returns:
            str: The string representation of the Square object.

        """
        return f"[Square] {self.__size}/{self.__size}"
