def no_c(my_string):
    msg = ""
    for char in my_string:
        if char != "c" and char != "C":
            msg += char
    return msg
