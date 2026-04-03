import os

# specify the path of the directory you want to list
path = "." # current directory

# Use the os module to list the directory contents
contents = os.listdir(path)

# print contents of the directory
for item in contents:
    print(item)