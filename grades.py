from students import find_student_by_id

def add_grade():
    #Add grades for student
    student_id = input("Enter Student ID: ")
    student = find_student_by_id(student_id)
    if not student:
        print("Student not found.")
        return

    subject = input("Enter Subject: ")
    try:
        grade = float(input("Enter Grade (5-10): "))
        if grade < 5 or grade > 10:
            print("Grade must be between 5 and 10")
            return
    except ValueError:
        print("Invalid grade. Please enter a number.")
        return

    student["grades"][subject] = grade
    print(f"Grade {grade} for {subject} added to student {student['name']}.")

def calculate_student_average():
    #Calculate average grade for one student
    student_id = input("Enter Student ID: ")
    student = find_student_by_id(student_id)
    if not student:
        print("Student not found.")
        return

    if not student["grades"]:
        print(f"Student {student['name']} has no grades yet.")
        return

    avg = sum(student["grades"].values()) / len(student["grades"])
    print(f"Student {student['name']} has an average grade of {avg:.2f}.")

def calculate_subject_average():
    #Calculate average grade for class course
    subject = input("Enter Subject: ")
    total = 0
    count = 0

    from students import students
    for student in students:
        if subject in student["grades"]:
            total += student["grades"][subject]
            count += 1

    if count == 0:
        print(f"No grades found for subject {subject}.")
    else:
        avg = total / count
        print(f"The average grade for {subject} is {avg:.2f}.")
