# WAP to input two angles from user and find third angle of tringle.

user_input1=int(input("Enter first angle:-"))
user_input2=int(input("Enter second angle:-"))

third_angle=180-(user_input1 + user_input2)

print(f"The Third angle of triangle is {third_angle}.")