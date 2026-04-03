# WAP to find the gratest of four numbers entered by the user.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(num1, "is gratest of four numbers")

elif(num2>num3 and num2>num1 and num2>num4):
    print(num2, "is gratest of four numbers")

elif(num3>num4 and num3>num1 and num3>num2):
    print(num3, "is gratest of four numbers")

else:
    print(num4, "is gratest of four numbers")