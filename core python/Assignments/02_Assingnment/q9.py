# WAP to swap two number without using third variable


a=int(input("Enter first number:-"))        # 10
b=int(input("Enter second number:-"))       # 5

a=a+b      # 10 + 5 = 15
b=a-b       # 15 - 5 = 10
a=a-b       # 15 - 10 = 5
print(f"After swapping a:-{a},b:-{b}")