from functools import reduce

l = [11, 33, 45678, 34, 56, 789]

def greater(a,b):
    if(a>b):
        return a
    return b

f = reduce(greater, l)
print(f)