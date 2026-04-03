class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    # def show(self):
    #     print(f"Complex number is: {self.r}r + {self.i}i")

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(4, 8)
# c1.show()
c2 = Complex(4, 2)
# c2.show()

print(f"Addrtron of two complex number rs: {c1 + c2}")