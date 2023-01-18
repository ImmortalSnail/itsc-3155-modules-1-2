# Gets strings, gets rid of spaces, initializes necessary variables
string = input("Input a string: ")
strip = string.replace(" ","")
upper = ""
lower = ""

# Sorts string into upper and lowercases
for x in strip:
    if x.isupper():
        upper += x
    else:
        lower += x

# Outputs results
print(lower+upper)