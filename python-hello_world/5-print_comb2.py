# To print number 00 to 99 in two digit
for num in range(100):
    print("{:02d}".format(num), end=", " if num != 99 else "\n")
