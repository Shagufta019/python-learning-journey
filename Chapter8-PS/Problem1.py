# Write a program using functions to find greatest of three numbers.
''' My code
a = 1
b = 2
c = 3

def greatest():
    if(a>b and a>c):
        print(a,"is greatest")
    elif(b>a and b>c):
        print(b, "is greatest")

    else:
        print(c, "is greatest")

greatest() '''



def greatest():
    if(a>b and a>c):
        return a
    
    
    elif(b>a and b>c):
        return b 

    else:
        return c
a = 1
b = 25
c = 3

print(greatest())