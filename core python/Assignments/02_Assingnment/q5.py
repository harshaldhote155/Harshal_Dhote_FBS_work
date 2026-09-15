# WAP to calculate selling price of book based on cost price and discount.

cp=int(input("enter the cost price:-"))
discount=int(input("enter the discount percentage:-"))

dis_amt=cp *discount/100
sp= cp- dis_amt
print("The selling price is",sp)
print("the dicounted amount is",dis_amt)