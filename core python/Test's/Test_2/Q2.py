# Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.

Digit_1=int(input("Enter the 1 digit:-"))
Digit_2=int(input("Enter the 2 digit:-"))
Digit_3=int(input("Enter the 3 digit:-"))

if(Digit_1 == 2 * Digit_2 and Digit_1 ==  Digit_3/ 2):
    print("You have done it!!!")

else:
    print("please try next time.")