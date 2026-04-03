class Employee:
    language = "Py" # This is a class attribute.
    salary = 1200000 

    def __init__(self, name, salary, language): # __init__: The constructor method that automatically initializes/call an object's attributes when the class is instantiated. Dunder method.
        self.name = name
        self.salary = salary
        self.language = language
        print("init constructor")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is P{self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee("Harry", 13000, "JavaScript")
print(harry.name, harry.salary, harry.language)