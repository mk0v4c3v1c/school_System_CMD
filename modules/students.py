import json
import os

DATA_FILE = "data/students.json"

def load_students():
    #Loading students from the JSON file.
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_students(students):
    #Saving students to the JSON file.
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    #Adding new students to the system.
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    student_id = input("Enter student ID: ")

    students = load_students()
    students.append({
        "id": student_id,
        "name": name,
        "age": age
    })
    save_students(students)
    print(f"Student {name} added successfully!")

def list_students():
    #Listing all students in the system.
    students = load_students()
    if not students:
        print("No students found!")
        return

    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")