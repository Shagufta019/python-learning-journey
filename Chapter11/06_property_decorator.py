class Employee:
    a = 1 

    @classmethod # A decorator that tells Python the next method belongs to the Class, not a specific instance.
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property # Turns the name method into a Getter. It allows you to access e.name like a simple variable instead of calling it like a function e.name()
    def name(self): # Combines two internal variables into one full name string.
        return f"{self.fname} {self.lname}"
    
    @name.setter # Defines a Setter. This runs automatically when you try to "assign" a value to name.
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Shagufta Jasim" # This triggers the @name.setter. It splits the string and creates e.fname ("Shagufta") and e.lname ("Jasim") behind the scenes.
print(e.fname, e.lname)

e.show() # Calling the class method