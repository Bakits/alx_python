#!/usr/bin/python3
if __name__ == "__main__":
    # declare two variable in different line
    a = 1
    b = 2

    # import module add
    add = __import__("add_0").add

    # print the value
    print("{} + {} = {}".format(a, b, add(a, b)))
