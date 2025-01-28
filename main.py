from modules.students import add_student, list_students
from modules.grades import add_grade, view_grades

def main_menu():
    while True:
        print("\n=== School Menu ===")
        print("1. Add Student")
        print("2. List Students")
        print("3. Add Grades")
        print("4. View Grades")
        print("5. Exit")
        print("=== Choose an option (1-5) ===")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            add_grade()
        elif choice == "4":
            view_grades()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()