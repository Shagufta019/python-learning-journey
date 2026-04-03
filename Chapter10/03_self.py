class Employee:
    language = "Py"
    salary = 1200000 

    def getInfo(self):
        print(f"The language is {self.language}. The salary is P{self.salary}")

    def greet(self):
        print("Good Morning")

harry = Employee()
# harry.language = "JavaScript"
# print(harry.language, harry.salary)
harry.greet()
harry.getInfo()
