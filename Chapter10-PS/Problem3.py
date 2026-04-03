class Demo:
    a = 4

o = Demo()
print(o.a) # prints the class attribute because intance attribute is not present.

o.a = 0 # Instance attribute is set
print(o.a) # prints the class attribute because intance attribute is present.

print(Demo.a)