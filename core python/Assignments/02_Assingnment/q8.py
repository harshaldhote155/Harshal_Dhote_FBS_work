# WAP to swap two numbers using third variable.

a=int(input("Enter first number:-"))                #10
b=int(input("Enter second number:-"))               #5

c=b                                                     # 5
b=a                                                     # 10
a=c                                                     # 5

print(f"After swapping a:-{a},b:-{b}")