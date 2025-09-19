my_dict = {}

while True:
    print("\nChoose your choice:")
    print("1. Add element to the dictionary")
    print("2. Delete element from the dictionary")
    print("3. Print the dictionary")
    print("4. Exit from the program")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        my_dict[key] = value
        print(f"Added ({key}: {value}) to the dictionary.")

    elif choice == 2:
        if my_dict:
            key = input("Enter the key to delete: ")
            if key in my_dict:
                del my_dict[key]
                print(f"Deleted key '{key}' from the dictionary.")
            else:
                print(f"Key '{key}' not found in the dictionary.")
        else:
            print("The dictionary is empty. Nothing to delete.")

    elif choice == 3:
        print("Current dictionary:", my_dict)

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please try again.")
