#!/usr/bin/python3
"""
    Creating the base class of all other classes for this project.
"""


class Base:
    """
    Base class representing a base object.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number of instances.
        id (int): Public instance attribute representing the object's ID.

    Methods:
        __init__(self, id=None): Constructor method to initialize the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base object.

        Args:
            id (int, optional): If provided, the ID to assign to the object. Defaults to None.
                               If not provided, auto-increments __nb_objects and assigns the new value to the ID.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
