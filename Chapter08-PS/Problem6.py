# inches ---> cms

def convert(inches):
    cms = inches * 2.54
    return round(cms, 2)

n = float(input("Enter the value of inches: "))
print("The corresponding value in cms is:",convert(n))

