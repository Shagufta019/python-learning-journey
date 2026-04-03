a = 89 # Global scope

def fun():
    global a # Use the global 'a'
    a = 3    # Update global value
    print("Local", a)

fun()
print("Global", a)