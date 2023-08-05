#!/usr/bin/python3
"""A base class for representing geometric entities."""


class BaseGeometry:
    """
    A base class for representing geometric entities.

    This class serves as a base class that other classes can inherit from to define specific
    geometric entities and their behavior.

    Attributes:
        None

    Methods:
        area(self):
            This method is not implemented in the base class and must be overridden in subclasses.
            It raises an Exception indicating that the specific implementation of area() is missing.

        integer_validator(self, name, value):
            Validates the given value as an integer for a specific attribute.

            Args:
                name (str): The name of the attribute being validated.
                value (int): The value to be validated as an integer.

            Raises:
                TypeError: If the value is not an integer, raises a TypeError with a descriptive message.
                ValueError: If the value is less than or equal to zero, raises a ValueError with a descriptive message.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer for a specific attribute.

        Args:
            name (str): The name of the attribute being validated.
            value (int): The value to be validated as an integer.

        Raises:
            TypeError: If the value is not an integer, raises a TypeError with a descriptive message.
            ValueError: If the value is less than or equal to zero, raises a ValueError with a descriptive message.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
