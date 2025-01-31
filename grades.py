from students import find_student_by_id, students
import csv

#Calculate averege all subjects
def calculate_all_subject_averages():
    from students import students
    subjects_totals = {}
    subjects_count = {}

    for student in students:
        for subject, grade in student["grades"].items():
            if subject not in subjects_totals:
                subjects_totals[subject] = 0
                subjects_count[subject] = 0
            subjects_totals[subject] += 1
            subjects_count[subject] += grade

    print("\n--- Average Grades by Subject ---")
    for subject, total in subjects_totals.items():
        avg = total/subjects_count[subject]
        print(f"{subject}: {avg:.2f}")
    print()

#Add grades for student
def add_grade():
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

#Calculate average grade for one student
def calculate_student_average():
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

#Calculate average grade for class course
def calculate_subject_average():
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

#Show bet student per subject
def best_student_in_subject(subject):
    best_student = None
    highest_grade = -1

    for student in students:
        if subject in student["grades"] and student["grades"][subject] > highest_grade:
            best_student = student
            highest_grade = student["grades"][subject]

    if best_student:
        print(f"Best student in {subject} is {best_student['name']} with grade of {highest_grade:.2f}.")
    else:
        print(f"No grades recorded for {subject}.")

 #Show top 3 student per average grades
def top_students():
    averages = []
    for student in students:
        grades = student["grades"].values()
        if grades:
            avg = sum(grades) / len(grades)
            averages.append((student["name"], avg))

    #Sort by averege grade
    top_3 = sorted(averages, key=lambda x: x[1], reverse=True)[:3]
    print("\n--- Top 3 Students ---")
    for i, (name, avg) in enumerate(top_3, 1):
        print(f"{i}. {name} - Average Grade: {avg:.2f}")


#Exporting student grades and subjects in CSV file
def export_averages_to_csv():
    averages = []
    for student in students:
        grades = student["grades"].values()
        if grades:
            avg = sum(grades) / len(grades)
            averages.append((student["id"], student["name"], avg))

    subject_averages = {}
    for student in students:
        for subject, grade in student["grades"].items():
            if subject not in subject_averages:
                subject_averages[subject] = []
            subject_averages[subject].append(grade)

    with open("averages.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Student Name", "Average Grade"])
        for student_id, name, avg in averages:
            writer.writerow([student_id, name, f"{avg:.2f}"])

        writer.writerow([])
        writer.writerow(["Subject", "Average Grade"])
        for subject, grades in subject_averages.items():
            writer.writerow([subject, f"{sum(grades) / len(grades):.2f}"])

    print("Averages successfully exported to 'averages.csv'.")