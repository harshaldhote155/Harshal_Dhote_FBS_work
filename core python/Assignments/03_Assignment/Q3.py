# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

user_input_1= int(input("Enter first angle:-"))
user_input_2= int(input("Enter second angle:-"))
user_input_3= int(input("Enter third angle:-"))

if(user_input_1 + user_input_2 + user_input_3 == 180):
    print("The Triangle is Valid.")
else:
    print("The Triangle is Invalid.")