# 4. Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.

area_of_one_wall=int(input("Enter the area of one wall:-"))
cost_of_interior_wall=int(input("Enter the cost of one interior wall:-"))

total_area= 4 * area_of_one_wall

total_cost= total_area * cost_of_interior_wall

print(f"The cost of painting is {total_cost} .")