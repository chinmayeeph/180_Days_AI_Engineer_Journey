# challenge/student_marks_analyzer.py

def get_valid_integer(prompt):
    """Safely gets a positive integer (> 0) from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Invalid input. The number must be greater than zero.\n")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid whole number.\n")


def get_valid_mark(prompt):
    """Safely gets a mark between 0 and 100 from the user."""
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid input. Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")


def calculate_average(marks):
    """Calculates the mathematical mean of a list of marks."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def get_grade_classification(average):
    """Determines the letter grade based on the average score."""
    if average >= 90:
        return "A (Excellent)"
    elif average >= 80:
        return "B (Very Good)"
    elif average >= 70:
        return "C (Good)"
    elif average >= 60:
        return "D (Pass)"
    else:
        return "F (Fail)"


def display_report(student_name, marks):
    """Calculates metrics and prints a clean markdown-styled report summary."""
    total = sum(marks)
    average = calculate_average(marks)
    highest = max(marks)
    lowest = min(marks)
    grade = get_grade_classification(average)
    
    print("\n" + "=" * 6 + f" STUDENT MARKS REPORT: {student_name.upper()} " + "=" * 6)
    print(f"Number of subjects: {len(marks)}")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Grade Classification: {grade}")
    print("=" * 40 + "\n")


def main():
    print("Welcome to the Robust Student Marks Analyzer!")
    
    try:
        while True:
            # Bonus 1: Student name
            student_name = input("Enter student name: ").strip()
            if not student_name:
                student_name = "Anonymous Student"
                
            # Step 1: Ask for number of subjects
            num_subjects = get_valid_integer("How many subjects? ")
            
            # Step 2 & 3: Collect and validate marks
            marks = []
            for i in range(1, num_subjects + 1):
                mark = get_valid_mark(f"Enter marks for subject {i}: ")
                marks.append(mark)
            
            # Step 4 & 5: Calculate and display the report (Includes Bonus 2)
            display_report(student_name, marks)
            
            # Bonus 3: Menu to analyze another student
            repeat = input("Would you like to analyze another student? (yes/no): ").strip().lower()
            if repeat not in ['y', 'yes']:
                print("Exiting program...")
                break
                
    except KeyboardInterrupt:
        # Handles unexpected termination (like hitting Ctrl+C) smoothly
        print("\nProgram interrupted by user.")
        
    finally:
        # Bonus 4: A finally block that displays a closing message
        print("\nThank you for using the Robust Student Marks Analyzer. Goodbye!")


# Run the application
if __name__ == "__main__":
    main()
