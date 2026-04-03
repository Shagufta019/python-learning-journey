# 27. Remove all duplicate elements from a list.

numbers = [1, 2, 2, 3, 4, 4, 5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List without duplicates:", result)