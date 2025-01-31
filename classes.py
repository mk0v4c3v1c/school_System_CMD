classes = []

#Add class
def add_class():
    class_name = input("Enter Class Name: ")
    classes.append({"name": class_name, "students": []})
    print(f"Class {class_name} has been added successfully!")

#Show classes
def list_classes():
    if not classes:
        print("No classes available.")
        return
    print("\n--- List of Classes ---")
    for cls in classes:
        print(f"Class Name: {cls['name']}, Students: {[student['name'] for student in cls['students']]}")
    print()
