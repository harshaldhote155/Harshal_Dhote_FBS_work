# WAP to accept an interger amount from user and tell minimum number of notes needed for representing that amount.

total_amount=int(input("enter the amount:-"))

note_2000=total_amount // 2000
remaing_amount=total_amount % 2000

note_500= remaing_amount // 500
remaing_amount= remaing_amount % 500

note_200= remaing_amount // 200
remaing_amount=remaing_amount % 200

note_100= remaing_amount // 100
remaing_amount=remaing_amount % 100

note_50= remaing_amount // 50
remaing_amount=remaing_amount % 50

note_20= remaing_amount // 20
remaing_amount=remaing_amount % 20

note_10= remaing_amount // 10
remaing_amount=remaing_amount % 10


print(f"2000:{note_2000},500:{note_500},200:{note_200},100:{note_100},50:{note_50},20:{note_20},10:{note_10}.")