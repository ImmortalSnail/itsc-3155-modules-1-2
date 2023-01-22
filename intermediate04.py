x = 0
num_list = []

while x < 5:
    num = input("Enter an integer: ")
    if num.lstrip("-").isdigit():
        x += 1
        num_list.append(int(num))
    else:
        print("Invalid input. Please enter an int.")

print("Your sum is", sum(num_list))