# 12. Count the total number of digits in an integer without converting it to a string.

n = int(input("Enter a number: "))

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        n = n // 10
        count += 1

print(f"The total number of digits in the given number is: {count}")