def even_num():
    list1 = input("Enter the list of numbers: ")
    split_list = list1.split()
    
    list2 = []
    for num in split_list:
        list2.append(int(num))
    print(f"Your list of numbers is {list2}")
    
    even_list = []
    for i in list2:
        if i % 2 == 0:
            even_list.append(i)
    
    return f"The even numbers are {even_list}."

print(even_num())