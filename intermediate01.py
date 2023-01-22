def get_unique_list(my_list):
    uniques = []
    for x in my_list:
        if uniques.count(x) == 0:
            uniques.append(x)
    return uniques


my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)