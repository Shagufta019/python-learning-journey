# 15. Generate and print the Fibonacci sequence up to N terms.
# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , ...

num = int(input("Enter number of terms: "))

a = 0 
b = 1

for i in range(num):
    print(a, end=" ")
    n = a + b
    a = b
    b = n