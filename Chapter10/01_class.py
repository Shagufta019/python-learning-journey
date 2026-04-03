# # class
# class Employee:
#     name = "Harry" #attribute
#     language = "Python" #attribute
#     salary = 120000 #attribut

# # Object
# harry = Employee()
# print(harry.name, harry.language)


class Employee:
    language = "Py" # This is class attribute
    salary = 1200000 # This is class attribute

harry = Employee()
harry.name = "Harry" # This is an object/intance attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan" # This is an object/instance attribute
print(rohan.name, rohan.language, rohan.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class. 
