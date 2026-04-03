# 20. Check if a string is a palindrome (reads the same forwards and backwards).

text = input("Enter a string of your choice: ")

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed text: ", reversed_text)

if (reversed_text == text):
    print(f"{text} is a palindrome ")

else:
    print(f"{text} is not a palindrome ")