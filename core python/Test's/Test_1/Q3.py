# 3. Write a program to accept distance in km and convert it into meters and
# centimeters both.

KM= int(input("Enter distance in km:-"))

meter= 1000 * KM

centimeter= 100000 * KM

print(f"The distance in meter is {meter}.")
print(f"The distance in centimeter is {centimeter}.")
