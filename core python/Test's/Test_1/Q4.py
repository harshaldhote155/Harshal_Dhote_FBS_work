# 4. Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)


Area_one_wall=int(input("Enter the Area of one wall:-"))
interior_cost=int(input("ENter the cost of interior wall:-"))
exterior_cost=int(input("Enter the cost of exterior wall:-"))

total_interior_cost= Area_one_wall * 8 * interior_cost
total_exterior_cost= Area_one_wall * 7 * exterior_cost

total_cost= total_interior_cost + total_exterior_cost

print(f"The total cost for painting building is {total_cost}.")