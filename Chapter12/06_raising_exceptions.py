a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if (b == 0):
    raise ZeroDivisionError("Hey our program ia not meant to divide numbers by zero")

else:
    print(f"THe division a/b is {a/b}")