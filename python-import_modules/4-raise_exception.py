def raise_exception():
    x = "this is a string"
    y = 10
    z = (
        x + y
    )  # This line will raise a TypeError since you can't concatenate a string and an integer.
