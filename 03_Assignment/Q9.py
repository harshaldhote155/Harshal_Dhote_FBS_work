
# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

user_input1=int(input("Enter mark of first subject:-"))
user_input2=int(input("Enter mark of second subject:-"))
user_input3=int(input("Enter mark of third subject:-"))
user_input4=int(input("Enter mark of fourth subject:-"))
user_input5=int(input("Enter mark of fifth subject:-"))

total_mark=int(input("Enter the total mark:-"))

percentage=((user_input1+user_input2+user_input3+user_input4+user_input5)/total_mark )*100

print(percentage)

if(percentage >= 75):
    print("Grade:- Distiction")
elif(percentage >= 60):
    print("Grade:- First Class")
elif(percentage >= 45):
    print("Grade:- Second Class")
elif(percentage >= 35):
    print("Grade:- Third Class")
else:
    print("You are fail.")
