# school_System_CMD
This is cmd school system python project

Project is based on adopting functional programming python skills and testing it.
This is a command-line application for managing a simple school system. It allows users to:

    *   Add, list, and remove students

    *   Manage subjects/classes

    *   Assign and view grades

    *   Calculate student and subject averages

    *   Export student data to a CSV file

The project is structured in a modular way, ensuring clean and maintainable code.

**Project Structure**

school_system/
│
├── main.py                 # Entry point of the application
├── students.py             # Handles student operations (add, list, remove)
├── classes.py              # Handles subject/class operations
├── grades.py               # Handles grade operations (assign, view, calculate averages)
├── utils.py                # Helper functions (data handling, validation, etc.)
├── menu.py                 # CLI menu logic
├── data/
│   └── students.csv        # Stores student data (generated dynamically)

**Features**

    Student Management: Add, list, and remove students.

    Class Management: Assign students to subjects/classes.

    Grade Management: Assign grades (validated between 5-10).

    Data Validation: Ensures proper formatting of student IDs and grade input.

    Average Calculation: Computes student and subject grade averages.

    CSV Export: Allows exporting student records.


**Installation & Setup**

1. Clone the Repository

`git clone https://github.com/yourusername/school_system.git
 cd school_system`

2. Install Dependencies (if needed)

`pip install -r requirements.txt  # If additional dependencies are required
`
3. Run the Application

`python main.py
`

**Usage**

When you run python main.py, a menu will appear with the following options:

--- School System Menu ---
1. Add Student
2. List Students
3. Add Class
4. List Classes
5. Add Grade to Student
6. Calculate Student Average
7. Calculate Subject Average
8. Export Students to CSV
9. Exit

Follow the prompts to perform various actions.