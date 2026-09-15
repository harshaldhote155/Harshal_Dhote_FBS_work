# 6. Write a program to calculate profit or loss.
selling_price= int(input("Enter the selling price:-"))
cost_price=int(input("Enter the cost price:-"))

Amount = selling_price - cost_price

if(Amount > 0):
    print(f"{Amount} is the profit Amount.")
else:
    print(f"{Amount} is the loss Amount.")


