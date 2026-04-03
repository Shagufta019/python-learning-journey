d = {} # Empty dictionary
print(d)

marks = { "Harry":100,
            "sita":79,
            "Gita":55,
            98:"Gita"
        }

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Harry": 99})
print(marks)

print(marks.get("Harryy")) # print none

# print(marks["Harryy"]) # return error

print(marks.pop("sita",79))
print(marks)
