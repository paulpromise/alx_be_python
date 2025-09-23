def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            shopping_list += [input("Enter the item to add: ")]
        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input("Enter item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
            else:
                print(f"{item_to_remove} not found in the list.")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f" - {item}")
            else:
                print("Shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()