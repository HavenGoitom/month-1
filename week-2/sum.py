def sum_numbers():
    list1 = input("Enter the list of numbers you want to add: ")
    split_list = list1.split()
    
    list2 = []
    for num in split_list:
        list2.append(int(num))
    print(f"Your list of numbers is {list2}")

    sum = 0
    for i in list2:
        sum += i
    
    return f"The sum is {sum}."

print(sum_numbers())

