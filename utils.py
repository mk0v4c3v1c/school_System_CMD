import csv

#Exporting list students into csv file
def export_students_to_csv(students):
    filename = input("Enter filename to export (e.g., students.csv): ")
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Grades"])
            for student in students:
                grades_str = ", ".join(f"{subject}: {grade}" for subject, grade in student["grades"].items())
                writer.writerow([student["id"], student["name"], student["age"], grades_str])
        print(f"Students exported successfully to {filename}")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
