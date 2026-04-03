# 8. Check if a given year is a leap year.

n = int(input("Enter the year: "))

if(n % 4 == 0 and n % 400 == 0):
    print(f"The year {n} is a leap year.")

else:
    print(f"The year {n} is not a leap year.")

