# Task 1: Create a Dictionary of Student Marks

def get_student_marks():
    """Creates a dictionary and retrieves student marks."""
    
    # Create a dictionary of student names and marks
    student_marks = {
        "Ava": 85,
        "Noah": 92,
        "Liam": 78,
        "Sophia": 89,
        "Ethan": 95
    }

    # Ask user for a student's name
    name = input("Enter the student's name: ").strip().capitalize()

    #Retrieve and display marks
    if name in student_marks:
        print(f"{name}'s marks: {student_marks[name]}")
    else:
        print(f"Student '{name}' not found in the records.")


if __name__ == "__main__":
    get_student_marks()
