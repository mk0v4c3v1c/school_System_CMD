from modules.students import load_students, save_students

def add_grade():
    #Add grade to a student.
    student_id = input("Enter student ID: ")
    students = load_students()

    # Find the student by ID
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        print("Student not found")
        return

    subject = input("Enter subject: ")
    grade = input("Enter grade: ")

    if "grades" not in students:
        student["grades"] = []

    student["grades"].append({"subject": subject, "grade": grade})
    save_students(students)
    print(f"Grade added for {student['name']} in {subject}.")

def view_grades():
    #View grades for a student.
    student_id = input("Enter student ID: ")
    students = load_students()

    #Find the student by ID
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        print("Student not found")
        return

    print(f"\n--- Grades for {student['name']} ---")
    if "grades" in students:
        for g in student["grades"]:
            print(f"Subject: {g['subject']}, Grade: {g['grade']}")
    else:
        print("No grades found.")