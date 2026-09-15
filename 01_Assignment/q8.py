# WAP to convert days into years, weeks, days.

total_days=int(input("Enter the total days:-"))   #385

year=total_days//365             #1year
remaining_days=total_days%365    #20days

week=remaining_days//7           #2 week
days=remaining_days% 7           #6 days

print(f"year:{year}, week:{week}, days:{days}")