age = int(input("Enter your age: "))


# If statement 1
if(age%2==0):
    print("It is even number")
# End of if statement 1

# If statement 2
if(age>=18):
    print("Your are above the age of consent.")
    print("Good for you.")

elif(age==0):
    print("You are entering 0, which is not a valid age.")


elif(age<0):
    print("You are entering an invalid age.")
    
else:
    print("You are below the age of consent.")
# End of if statement 1


print("End of program")