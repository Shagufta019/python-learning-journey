s1 = {1, 8, 45, 6}
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)
print(s2-s1)

print(s1 ^ s2) #Returns elements that are in either set but not both.
print(s1.symmetric_difference(s2)) #symmetric_difference

print(s1.issubset(s2)) #false
print(s2.issubset(s1)) #false


s1 = {1, 8}
s2 = {7, 8, 1, 78}

print(s1.issubset(s2)) #true
print(s2.issuperset(s1)) #true