from modules.students import add_student, list_students

def main_menu():
    while True:
        print("\n=== School Menu ===")
        print("1. Add Student")
        print("2. List Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()