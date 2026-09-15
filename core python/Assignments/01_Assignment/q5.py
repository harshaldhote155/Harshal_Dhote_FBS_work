# WAP to enter P,R,T and calculate CI.

p=int(input("Enter the principle amount:-"))
r=int(input("Enter the Rate of interest:-"))
t=int(input("Enter the time period:-"))

ci=int(p*(1+r/100)**t - p)

print("The Compound interest is",ci)