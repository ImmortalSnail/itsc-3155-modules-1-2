def char_count(string):
    dict = {}
    string = string.replace(" ",'')

    for x in range(len(string)):
        dict[string[x]] = 0

    for x in range(len(string)):
        dict[string[x]] += 1

    return dict

print(char_count(input("Please enter a string: ")))