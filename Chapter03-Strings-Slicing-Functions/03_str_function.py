a = "hello world"

print(a.upper())
print(a.lower())
print(a.title()) # this will capitalize the first letter of each word and make the rest of the letters lowercase.   
print(a.capitalize()) # this will capitalize the first letter of the string and make the rest of the letters lowercase.

a = "hELlo wOrld"
print(a.swapcase())

a = "hello world"
print(a.find("h")) # this will return the index of the first occurrence of the substring "ld" in the string "hello world".
print(a.find("l"))

print(a.replace("world", "Python"))

a= " hello world "
print(a.strip()) # this will remove any leading and trailing whitespace from the string " hello world ".

a= " hel lo world "
print(a.split()) # this will split the string "hello world" into a list of words, using whitespace as the delimiter.
print(a.count("l"))

a = 'hello world'
print(a.startswith("h")) # this will return True if the string "hello world" starts with the substring "h", and False otherwise.
print(a.endswith("d")) # this will return True if the string "hello world" ends with the substring "d", and False otherwise.    
print(''.join(a))

