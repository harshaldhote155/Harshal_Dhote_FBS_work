# WAP to calculate total salary of empolyee based on basic, da= 10% of basic,ta=12% of basic,hra=15% of basic.

basic=int(input("enter the basic pay of employee;-"))

da=basic * (10/100)
ta= basic * (12/100)
hra = basic * (15/100)

total_salary= basic + da + ta + hra
print("the total salary is",total_salary)