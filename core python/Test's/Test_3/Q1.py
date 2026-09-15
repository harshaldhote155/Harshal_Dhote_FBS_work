# 1. Write a program to print first n prime numbers

n = int(input("Enter value of n: "))

count = 0

for i in range(2, 10000):

    if count == n:
        break

    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        count += 1