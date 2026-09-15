# WAP to reverse three digit number

num=int(input("Enter three digit number:-"))  #385

d1=num%10  
remaining_num=num//10

d2=remaining_num%10
remaining_num=remaining_num//10

d3=remaining_num%10
remaining_num=remaining_num//10

print(f"Digit:{d1}{d2}{d3}")

