my_list = [12,3,5,6,3.9]

while True:
    print("\nChoose your choice:")
    print("1. Sort the list")
    print("2. Reverse the list")
    print("3. Count elements in the list")
    print("4. Exit the program")

    choice = int(input("Your choice: "))

    if choice == 1:
        my_list.sort()
        print("Sorted list:", my_list)

    elif choice == 2:
        my_list.reverse()
        print("Reversed list:", my_list)

    elif choice == 3:
        print("Total number of elements in the list:", len(my_list))

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
