a = "{} is a {}".format("Apple", "fruit")
print(a) # Output:Apple is a fruit

a = "{1} is a {0}".format("Apple", "fruit")
print(a) # Output:fruit is a Apple

a = "{0} is a {0}".format("Apple", "fruit")
print(a) # Output:Apple is a Apple
