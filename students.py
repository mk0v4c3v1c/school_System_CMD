students = []

#Generating unique ID for student
def generate_student_id():
    count = len(students)
    return f"ID_{count:02d}"

#Add students
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        return
    students.append({"id": student_id, "name": name, "age": age, "grades": {}})
    print(f"Student {name} has been added successfully with ID {student_id}!")

#List students
def list_students():
    if not students:
        print("No students available.")
        return
    print("\n--- List of Students ---")
    for student in students:
        grades_str = ", ".join(f"{subject}: {grade}" for subject, grade in student["grades"].items())
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grades: {grades_str if grades_str else 'No grades yet'}")
    print()

#Find student
def find_student_by_id(student_id):
    return next((s for s in students if s["id"] == student_id), None)

#Find student by name
def search_student_by_name():
    query = input("Enter part of the student's name: ").lower()
    results = [student for student in students if query in student["name"].lower()]

    if results:
        print("\n--- Search Results ---")
        for student in results:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    else:
        print("No students found with that name.")

