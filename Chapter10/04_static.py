class Employee:
    language = "Py"
    salary = 1200000 

    def getInfo(self):
        print(f"The language is {self.language}. The salary is P{self.salary}")

    @staticmethod # A decorator used to define a method that belongs to a class but does not access or modify the class or instance state (no self or cls).
    def greet():
        print("Good Morning")

harry = Employee()
# harry.language = "JavaScript"
# print(harry.language, harry.salary)
harry.greet()
harry.getInfo()
