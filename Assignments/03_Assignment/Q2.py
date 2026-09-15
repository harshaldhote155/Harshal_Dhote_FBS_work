# 2. Write a program to input any alphabet and check whether it is vowel or consonant.

user_input=str(input("Enter the Alphabet you want to check:-"))

if(user_input in "aeiou"):
    print("It is a Vowel.")

else:
    print("It is a Consonant.")