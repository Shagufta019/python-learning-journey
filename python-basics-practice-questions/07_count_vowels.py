# 18. Count the number of vowels (a, e, i, o, u) in a given string.

s = input("Enter a string: ")

vowels = ("a", "e", "i", "o", "u")
count = 0

for char in s.lower():
    if char in vowels:
        print(char, end=" ")
        count += 1

print("\nTotal vowels:", count)