# WAP to filter a list of numbers which are divisible by 5.

def divisible(n):
    if(n%5 == 0):
        return True
    return False

l = [1, 4, 5, 10, 8 , 15, 20]

f = list(filter(divisible, l))

print(f)