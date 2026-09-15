# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


base_price=float(input("Enter the price of ticket per person:-"))
total=0

print("Enter ages of people")
for i in range(1,6):
    age=int(input(f"Enter age of person {i}:-"))

    if(age < 12):
        amount= base_price-(base_price * (30/100))

    elif( age > 59):
        amount= base_price -(base_price * (50/100))

    else:
        amount=base_price
    total=total+amount
print(total)        

# base_price :- per person original ticket
# amount :- discount ke baad ek person ka ticket
# total :- 5 logon ke tickets ka final total