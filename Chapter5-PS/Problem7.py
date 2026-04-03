# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
# If the names of 2 friends are same?

dict = {}

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
dict.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
dict.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
dict.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
dict.update({name: lang})

print(dict)