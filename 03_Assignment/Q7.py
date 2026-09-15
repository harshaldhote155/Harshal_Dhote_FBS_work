# 7. Write a program to check if user has entered correct userid and password.

user_input_id=str(input("Enter the Userid:-"))
user_input_pass=str(input("Enter the Password:-"))

user_id = "admin@123"
password = "levi@123"

if( user_input_id == user_id and user_input_pass == password ):
    print("User is Valid")

else:
    print("User is Invalid.")