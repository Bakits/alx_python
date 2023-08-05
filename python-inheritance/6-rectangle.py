#!/usr/bin/python3
"""A class representing a rectangle, inheriting from BaseGeometry."""
BaseGeometry = __import__("5-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    This class inherits from the BaseGeometry class and provides functionality to represent a rectangle.
    It includes validation for positive integer values for width and height.

    Attributes:
        __width (int): The width of the rectangle (private attribute).
        __height (int): The height of the rectangle (private attribute).

    Methods:
        __init__(self, width, height):
            Initializes a new Rectangle object with the given width and height.

        __str__(self):
            Returns a string representation of the Rectangle in the format [Rectangle] width/height.

    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is not a positive integer.

        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle in the format [Rectangle] width/height.

        Returns:
            str: The string representation of the Rectangle object.

        """
        return f"[Rectangle] {self.__width}/{self.__height}"
