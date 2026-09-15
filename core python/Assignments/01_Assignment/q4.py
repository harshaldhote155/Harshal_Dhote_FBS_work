#WAP to enter P,R,T and calculate SI.

principle = int(input("enter principle amount:-"))
rate_of_interest=int(input("Enter rate of interest:-"))
time = int(input("enter Time period:-"))

si=int((principle*rate_of_interest*time)/100)

print("The simple interest is",si)


