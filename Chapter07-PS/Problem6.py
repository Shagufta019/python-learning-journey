n = int(input("Enter a number: "))

# i = 1
# fact = 1
# while(i<=n):
#     fact = fact * i
#     i = i + 1
# print(fact)

# using for loop
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)