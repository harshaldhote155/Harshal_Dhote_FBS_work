# WAP to find sum of three-digit number.

num=int(input("Enter three digit number:-"))  #385

d1=num%10                                       #5
remaining_num=num//10                           #38

d2=remaining_num%10                             #8
remaining_num=remaining_num//10                 #3

d3=remaining_num%10                             #3
remaining_num=remaining_num//10                 #0

print(f"Digit1:{d1},Digit2:{d2},Digit3:{d3}")

sum=d1+d2+d3

print("The sum of Three digit is",sum)