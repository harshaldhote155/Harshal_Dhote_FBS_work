# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

product_1=int(input("Enter the price of 1 product:-"))
product_2=int(input("Enter the price of 2 product:-"))
product_3=int(input("Enter the price of 3 product:-"))
product_4=int(input("Enter the price of 4 product:-"))
product_5=int(input("Enter the price of 5 product:-"))


price = product_1 + product_2 +product_3 + product_4 + product_5

gst= (price * 18 )/ 100

total_price=price + gst

print(f"Total bill is {total_price}.")