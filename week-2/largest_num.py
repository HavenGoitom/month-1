def largest_num():
    list1 = input("Enter the list of numbers: ")
    split_list = list1.split()
    
    list2 = []
    for num in split_list:
        list2.append(int(num))
    print(f"Your list of numbers is {list2}")

    largest_num = max(list2)
     
    return f"The largest number is {largest_num}."

print(largest_num())