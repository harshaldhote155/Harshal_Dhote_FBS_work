
# wap to convert the time entered in hh,min,sec into second.
hr=int(input("Enter Hour:-"))
min=int(input("Enter minute:-"))
sec=int(input("Enter second:-"))

total_second=(hr*3600)+(min*60)+sec

print("The total second is",total_second)