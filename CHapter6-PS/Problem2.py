# WAP to find out whether a student has passed pr failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

phy = int(input("Enter marks of pysics: "))
chem = int(input("Enter marks of chemistry: "))
math = int(input("Enter marks of maths: "))

total_percentage = ((phy+chem+math) / 300) * 100

print(total_percentage)

if(total_percentage>=40 and phy>=33 and chem>=33 and math>=33 ):
    print("You are passed")

else:
    print("You are fail")