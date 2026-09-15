#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender=input("Enter Gender(M/F):-")
age=int(input("enter age:-"))

if(gender=="F"):
    if(age>=18):
        print("Girl is eligible for Marriage.")
    else:
        print("Girl is not eligible for marriage.")

else:
    if(age>=21):
        print("Boy is eligible for marriage.")
    else:
        print("Boy is not eligible for marriage.")
