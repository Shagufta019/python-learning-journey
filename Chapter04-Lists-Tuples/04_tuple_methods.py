a = (1, 45, 342, 5677, 87.67, False, "Rohan")
print(a)

b = a.count(45)
print(b)

print(a.index(87.67)) # If value not found then it will givve error

print(a[0])

print(a[1:]) #slicing
print(a[:]) # It will print all values
print(a[1:5]) # From 1 to 4

t1 = (4, 6, 7)
t2 = (1, 4, 9)
print(t1 + t2) # Concatenation

t = (1, 2)
print(t * 3) # Repetition 3 times

t = (10, 20, 30) # membership
print(20 in t)      # True
print(50 not in t)  # True

a, b, c = (10, 20, 30) # Unpacking
print(a)  # 10
print(b)  # 20