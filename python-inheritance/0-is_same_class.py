#!/usr/bin/python3
"""Check if the object is exactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object with.

    Returns:
        bool: True if the object is an instance of the specified class, False otherwise.
    """
    return type(obj) is a_class
