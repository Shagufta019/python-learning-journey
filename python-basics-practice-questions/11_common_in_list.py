# 32. Find the common elements between two lists.

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [1, 4, 9, 16, 25, 36, 49, 64, 81]

common = []

# for item in l1 :
#     if item in l2:
#         common.append(item)

common = list(set(l1) & set(l2))

print("Common elements:", common)