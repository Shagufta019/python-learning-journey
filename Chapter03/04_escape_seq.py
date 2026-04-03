a = "Hello\nWorld" #new line
print(a)

a = "Hello\tWorld" #tab space
print(a)

a = "Hello World it\'s a beautiful day" #this will ignore the new line character and print the string in one line.
print(a)

a = "Hello \"World\""
print(a)

a = "Helloo\b World"
print(a)

print(r"Hello\nWorld") # this will print the string "Hello\nWorld" as it is, without interpreting the escape sequence \n as a new line character. The r before the string indicates that it is a raw string, which means that backslashes are treated as literal characters and not as escape characters.       

print("Hello \\ World")

print("Hello\rWorld") #overwrites Hello 
