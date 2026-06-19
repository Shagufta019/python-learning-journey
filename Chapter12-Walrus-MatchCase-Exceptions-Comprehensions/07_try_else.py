try:
    print(int(input("Enter a number: ")))


except Exception as e: # Runs only if an errors occurred in the try block.
    print(e)

else:
    print("You are inside else.") # Runs only if no errors occurred in the try block.