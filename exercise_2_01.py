# Gets string
string = input("Input a string: ")

# Prints string backwards
for x in range(len(string)):
    if x == 0:
        pass
    else:
        print(string[-x], end="")

# Prints first char
print(string[0])

# https://realpython.com/python-pass/ used this to learn how to do nothing in python