def get_combined_dict(my_dict_1, my_dict_2):
    combined_dict = {}
    list1 = my_dict_1.keys()
    list2 = my_dict_2.keys()

    for x in list1:
        if x in my_dict_1 and x in my_dict_2:
            combined_dict[x] = my_dict_1[x] + my_dict_2[x]


    return combined_dict


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)