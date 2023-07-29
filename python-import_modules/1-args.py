import sys


def main():
    # Number of arguments
    num_args = len(sys.argv) - 1
    # Output the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    # Output the list of arguments
    if num_args > 0:
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
