for i in range(12):
    if i == 0 or i == 11:
        print("*" * 22)
    else:
        print(" " * (22 - i) + "*")
