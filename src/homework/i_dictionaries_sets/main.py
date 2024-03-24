def display_menu():
    print("Inventory Menu\n")
    print("1- Add or Update Item")
    print("2- Delete Item")
    print("3- Exit")

def add_or_update_item():
    # Implement add or update item functionality
    print("Adding or Updating Item...")

def delete_item():
    # Implement delete item functionality
    print("Deleting Item...")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_or_update_item()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()