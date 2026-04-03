class Student:

    def __init__(self, phy, chem, math):
        self.sub1 = phy
        self.sub2 = chem
        self.sub3 = math
        
        self.marks = [self.sub1, self.sub2, self.sub3]

        print(f"Marks in Physics is {self.sub1}, Marks in Chemistry is {self.sub2}, Marks in Maths is {self.sub3}.")

    def get_avg(self):
        total = sum(self.marks)
        return total / len(self.marks)
    
            

s1 = Student(78, 98, 45)
print(round(s1.get_avg()))


