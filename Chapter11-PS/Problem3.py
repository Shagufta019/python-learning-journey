class Employee:
    salary = 234
    increment = 20

    @property # Getter The @property decorator allows you to access this like a variable (e.salaryAfterIncrement) instead of calling a function with parentheses.
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1) * 100

e = Employee()
print(e.salaryAfterIncrement) # 280.8 (234 + 20%)
print(e.increment)