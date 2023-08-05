#!/usr/bin/python3
"""Check if the object's class is a subclass of the specified class"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of a class that inherited from the specified class,
              otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
