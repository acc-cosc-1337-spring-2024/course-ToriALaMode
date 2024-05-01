from homework.c_decisions.decisions import sum_odd_numbers
from homework.d_repetition.repetition import get_factorial

def show_menu():
    print("Homework 3 Menu")
    print("1-Factorial")
    print("2-Sum odd numbers")
    print("3-Exit")

def validate_number(num, min_val, max_val):
    return min_val < num < max_val

def get_valid_number(prompt, min_val, max_val):
    while True:
        try:
            num = int(input(prompt))
            if validate_number(num, min_val, max_val):
                return num
            else:
                print("Please enter a number between {} and {}.".format(min_val, max_val))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    while True:
        show_menu()
        choice = get_valid_number("Enter your choice: ", 1, 4)
        
        if choice == 1:
            num = get_valid_number("Enter a number (0-9): ", 0, 10)
            print("Factorial of {} is: {}".format(num, get_factorial(num)))
        elif choice == 2:
            num = get_valid_number("Enter a number (0-99): ", 0, 100)
            print("Sum of odd numbers up to {} is: {}".format(num, sum_odd_numbers(num)))
        elif choice == 3:
            exit_choice = input("Do you want to exit? (yes/no): ").lower()
            if exit_choice == "yes":
                print("Exiting...")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()