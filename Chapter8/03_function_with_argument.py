# Function with argument, (name, ending) parameters, ("Harry", "Thank You!") arguments.
'''
def goodDay(name, ending):
    print(f"Good Day, {name}!")
    print(ending)

goodDay("Harry", "Thank You!")
goodDay("Carry", "Thank You!") '''


def goodDay(name, ending):
    print(f"Good Day, {name}!")
    print(ending)
    return "ok" # return value assign to a

a = goodDay("Harry", "Thank You!")
print(a)