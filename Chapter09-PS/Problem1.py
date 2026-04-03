with open("poem.txt", "w") as f:
    st = "Twinkle, Twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky."
    f.write(st)



with open("poem.txt", "r") as f:
    poem = f.read()
    if("twinkle" in poem.lower()):
        print("The word twinkle is present in the content")

    else:
        print("The word twinkle is not present in the content")


    

