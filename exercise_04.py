# By Ronnie Hampton
# Variables
list_size = int(input("Enter list size: "))
list = []

# Adds to list
for x in range(list_size):
    list.append(float(input("Please enter a float: ")))

#Prints result
print(str(list))
print((sum(list) / list_size))