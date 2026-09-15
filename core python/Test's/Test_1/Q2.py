# 2. Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)

principal= int(input("enter the principal"))
rate_of_interest= int(input("enter the rate_of_interest"))
Time= int(input("enter the Time"))

simple_interest= (principal * rate_of_interest * Time)/100

print(f"The Simple interst is {simple_interest}")
