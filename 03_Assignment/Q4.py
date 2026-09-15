# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not. 

a = int(input("Enter first side:-"))
b = int(input("Enter second side:-"))
c = int(input("Enter third side:-"))

if( a + b > c and b + c > a and c + a > b ):
    print("triangles is valid.")

else:
    print(" triangle is not valid.")