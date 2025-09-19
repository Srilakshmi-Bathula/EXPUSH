my_list = []

while True:
    print("\nChoose your choice:")
    print("1. Add element")
    print("2. Delete element")
    print("3. Print list")
    print("4. Exit Program")
    choice = int(input("Enter Your choice: "))

    if choice == 1:
        num_add = input("Enter the element to add: ")
        my_list.append(num_add)
        print(f"{num_add} added to the list.")

    elif choice == 2:
        if my_list:
            num_del = input("Enter the element to delete: ")
            if num_del in my_list:
                my_list.remove(num_del)
                print(f"{num_del} removed from the list.")
            else:
                print(f"{num_del} not found in the list.")
        else:
            print("The list is empty. Nothing to delete.")

    elif choice == 3:
        print("Current list:", my_list)

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
