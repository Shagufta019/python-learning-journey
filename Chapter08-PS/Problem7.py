def remove(l, word):
    n = [] #empty list to store our processed results
    for item in l:
        if not(item == word):
            # 1. Take the item, strip 'a' and 'n' from its start and end
            # 2. Use .append() to add that cleaned string into our list 'n'
            n.append(item.strip(word)) 
    return n
    
l = ["Harry", "Rohan", "Shubham", "an", "Anna", "Sita"]
print(remove(l, "an"))