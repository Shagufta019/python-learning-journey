class Vector:
    def __init__(self, l):
        self.l = l 

    def __add__(self, v2):
        newList = [self.l[i] + v2.l[i] for i in range(len(self.l))]
        return Vector(newList)

    def __mul__(self, v2):
        dot_product = 0
        for i in range(len(self.l)):
            dot_product += self.l[i] * v2.l[i]
        return dot_product

    def __str__(self):
        return f"Vector({self.l})"

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")

print(f"Sum: {v1 + v2}")

print(f"Dot Product: {v1 * v2}")