from homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog1_or_prog2, get_students_who_took_prog2_not_prog_1


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


def print_menu():
    #Inventory Menu
    print("Inventory Menu\n")
    #1-Students who took prog1 and prog2
    print("1-Students who took prog1 and prog2")
    #2-Students who took prog2 only
    print("2-Students who took prog1 or prog2")
    #3-Students who took prog1 not prog2
    print("3-Students who took prog1 not prog2")
    #4-Students who took prog2 not prog1
    print("4-Students who took prog2 not prog1")
    #5-Exit
    print("5-Exit")

def main_menu():
    # Define prog1 and prog2 dictionaries
    prog1 = {'Student1', 'Student2', 'Student3'}
    prog2 = {'Student3', 'Student4', 'Student5'}


#The program runs until the user chooses option 5.
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            result = get_students_who_took_prog1_and_prog2(prog1, prog2)
            print("Students who took prog1 and prog2:", result)
        elif choice == '2':
            result = get_students_who_took_prog1_or_prog2(prog1, prog2)
            print("Students who took prog1 or prog2:", result)
        elif choice == '3':
            result = get_students_who_took_prog1_not_prog_2(prog1, prog2)
            print("Students who took prog1 not prog2:", result)
        elif choice == '4':
            result = get_students_who_took_prog2_not_prog_1(prog1, prog2)
            print("Students who took prog2 not prog1:", result)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try a number between 1 and 5.")
if __name__ == "__main_menu__":
    main_menu()



    
    



