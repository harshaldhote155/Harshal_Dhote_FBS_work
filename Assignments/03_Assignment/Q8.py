#  8. Write a program to prompt user to enter userid and password. After verifying
#  userid and password display a 4 digit random number and ask user to enter the
#  same. If user enters the same number then show him success message otherwise
#  failed. (Something like captcha)


import random

user_input_id=str(input("Enter the Userid:-"))
user_input_pass=str(input("Enter the Password:-"))


user_id = "admin@123"
password = "levi@123"

if( user_input_id == user_id and user_input_pass == password ):
    

    captcha=random.randint(1000,9999) 
    print(f"{captcha} is your captcha verification code.")

    user_captcha=int(input("Enter the code shown above:-"))

    if(captcha == user_captcha):
        print("User is Valid")
        
        print("Sucessfully login!!!")

    else:
        print("captcha invalid")
else:
    print("user is Invalid.")