#!/usr/bin/python3
"""Module containing is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or an instance of a class that inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object with.

    Returns:
        bool: True if the object is an instance of the specified class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
