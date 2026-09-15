# 1. Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

length= int(input("Enetr The length:-"))
breadth= int(input("Enetr The breadth:-"))
radius= int(input("Enetr The radius:-"))

Area_of_rectangle= length * breadth
Area_of_circle= (3.14 * radius ** 2)/2

Total_area= Area_of_circle +Area_of_rectangle

print(f"The Area of Figuare is {Total_area}.")

perimeter= length + length + breadth + (3.14 * radius)

print(f"The perimeter of Figuare is {perimeter}.")