students = []

def generate_student_id():
    #Generating unique ID for student
    count = len(students)
    return f"ID_{count:02d}"

def add_student():
    #Add students
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        return
    students.append({"id": student_id, "name": name, "age": age, "grades": {}})
    print(f"Student {name} has been added successfully with ID {student_id}!")

def list_students():
    #List students
    if not students:
        print("No students available.")
        return
    print("\n--- List of Students ---")
    for student in students:
        grades_str = ", ".join(f"{subject}: {grade}" for subject, grade in student["grades"].items())
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grades: {grades_str if grades_str else 'No grades yet'}")
    print()

def find_student_by_id(student_id):
    #Find student
    return next((s for s in students if s["id"] == student_id), None)
