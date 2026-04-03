# 17. Find the length of a string without using the built-in len() function

text = input("Enter a string: ")

counter = 0
for char in text:
    counter += 1

print(f"Length of {text} is {counter}")
    