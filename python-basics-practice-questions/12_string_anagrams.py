# 40. Write a function that checks if two strings are anagrams of each other.

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

t1 = "".join(text1.split()).lower()
t2 = "".join(text2.split()).lower()

sorted_t1 = sorted(t1)
sorted_t2 = sorted(t2)

if(sorted_t1 == sorted_t2):
    print(f"{text1} and {text2} are anagrams of each other.")

else:
    print(f"{text1} and {text2} are not anagrams of each other.")
