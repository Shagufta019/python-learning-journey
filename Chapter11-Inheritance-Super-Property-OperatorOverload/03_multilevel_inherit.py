class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Puppy(Dog):
    def weep(self):
        print("Puppy is dog's child")

# Creating an instance of the lowest child class
c = Puppy()

c.bark() # Inherited from Dog

