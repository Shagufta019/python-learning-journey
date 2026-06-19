try:
    print(int(input("Enter a number: ")))


except Exception as e:
    print(e)

finally:
    print("You are inside the finally block.") # This block will always execute.


# (it can interrupt a return) If you have a return statement inside a try block, you might think the function ends immediately. But Python is designed to "pause" that return, run the finally block, and then actually finish the function