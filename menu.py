from students import add_student, list_students
from classes import add_class, list_classes
from grades import add_grade, calculate_student_average, calculate_subject_average
from utils import export_students_to_csv
from students import students

def menu():
    """CMD meni"""
    while True:
        print("\n--- School System Menu ---")
        print("1. Add Student")
        print("2. List Students")
        print("3. Add Class")
        print("4. List Classes")
        print("5. Add Grade to Student")
        print("6. Calculate Student Average")
        print("7. Calculate Subject Average")
        print("8. Export Students to CSV")
        print("9. Exit")
        choice = input("Choose an option (1-9): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            add_class()
        elif choice == "4":
            list_classes()
        elif choice == "5":
            add_grade()
        elif choice == "6":
            calculate_student_average()
        elif choice == "7":
            calculate_subject_average()
        elif choice == "8":
            export_students_to_csv(students)
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
