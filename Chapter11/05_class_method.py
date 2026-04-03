class Employee:
    a = 1 # This is a Class Attribute (shared by all instances)

    @classmethod #The @classmethod looks at the class variable (a = 1), ignoring the instance variable (a = 45) created on the object.
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show() # Calling the class method