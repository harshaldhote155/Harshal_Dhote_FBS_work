# WAP to find roots of a quadratic eqution.

a=int(input("enter value of a:-"))
b=int(input("enter value of b:-"))
c=int(input("enter value of c:-"))

d=(b**2 - 4*a*c) ** 0.5

x=(-b+d)/(2*a)
y=(-b-d)/(2*a)

print("The first root is",x)
print("The second root is",y)