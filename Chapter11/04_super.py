class Employee:
    def __init__(self):
        print("Employee constructor running")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Programmer constructor running")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Manager constructor running")
    c = 3

o = Manager()