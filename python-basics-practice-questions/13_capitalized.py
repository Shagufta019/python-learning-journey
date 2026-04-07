# 22. Capitalize the first character of each word in a string.

text = "hello world"
result = ' '.join(word.capitalize() for word in text.split())
print(result)