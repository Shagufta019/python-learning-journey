words = ["Harry", "Carry", "Marry"]

with open("5file.txt", "r") as f:
    content = f.read()

for word in words:
    # We update 'content' itself each time!
    content = content.replace(word, "#" * len(word))

with open("5file.txt", "w") as f:
    f.write(content)