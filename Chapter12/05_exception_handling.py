# Exception Handling : It is designed to prevent your program from "crashing" (stopping abruptly) when a user provides unexpected input or an error occurs.

try:
    print(int(input("Enter a number: ")))

except ValueError as v:
    print(v)

except TypeError as t:
    print(t)

except Exception as e:
    print(e)

print("Thank You")