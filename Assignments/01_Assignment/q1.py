#WAP to calculate the percentage of student based on marks of any 5 subject.

user_input1=int(input("enter mark of first subject:-"))
user_input2=int(input("enter mark of second subject:-"))
user_input3=int(input("enter mark of third subject:-"))
user_input4=int(input("enter mark of fourth subject:-"))
user_input5=int(input("enter mark of fifth subject:-"))

total_mark=int(input("enter total mark:-"))

sum = user_input1 + user_input2 + user_input3 + user_input4 + user_input5 

percentage = sum / total_mark * 100

print(percentage)

