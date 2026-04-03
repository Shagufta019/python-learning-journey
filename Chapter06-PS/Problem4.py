# Write a program which finds out whether a given username contains less than 10 characters or not.

username = input("Enter your username: ")

if(len(username)<10):
    print("This username contains less than 10 characters")

else:
    print(username)