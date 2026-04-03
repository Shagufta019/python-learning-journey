class Programmer:
    company = "Microsoft" #class attribute (same for all)
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

employee1 = Programmer("Harry", 1234335, 87010)
print(employee1.name, employee1.salary, employee1.pin)

employee2 = Programmer("Rohan", 678909, 12345)
print(employee2.name, employee2.salary, employee1.pin)

