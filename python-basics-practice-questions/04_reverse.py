# 13. Reverse a given integer using a loop (e.g., 123 becomes 321).

n = 123
reversed_num = 0

while (n>0):
    x = (n%10)
    reversed_num = (reversed_num * 10) + x
    n = n // 10

print(reversed_num)