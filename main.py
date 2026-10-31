# Import User Defined Functions
from functions import (
    calculate_total,
    calculate_average,
    get_grade,
    check_result,
    student_summary,
    add_student,
    update_marks,
    remove_student,
    print_report,
    class_statistics
)

# Starter Data
students = {
    "S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
    "S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
    "S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
    "S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
    "S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}}
}

# Main Function
def main():

    # Task 1: One Student
    print("Task 1: One student")

    print(student_summary(students["S101"]))

    print(check_result(students["S102"]["marks"]))
    print(check_result(students["S102"]["marks"], pass_mark=35))
    print(check_result(students["S102"]["marks"], 35))

    # Task 2: Report
    print("\nTask 2: Report")

    print_report(students)

    # Task 3: Update Marks
    print("\nTask 3: Update marks")

    print(update_marks(students, "S102", Maths=55))

    print(update_marks(students, "S999", Maths=55))

    corrections = {"Python": 50, "Stats": 58}

    print(update_marks(students, "S102", **corrections))

    print(student_summary(students["S102"]))

    # Task 4: Add Student
    print("\nTask 4: Add student")

    print(
        add_student(
            students,
            "S106",
            "Farhan",
            Python=70,
            Maths=35,
            Stats=74
        )
    )

    print(
        add_student(
            students,
            "S101",
            "Zara",
            Python=80,
            Maths=80,
            Stats=80
        )
    )

    print(students["S106"])

    # Task 5: Remove Student
    print("\nTask 5: Remove student")

    print(remove_student(students, "S104"))

    print(remove_student(students, "S104"))

    print(len(students))

    # Task 6: Final Report and Statistics
    print("\nTask 6: Final report and statistics")

    print_report(students)

    stats = class_statistics(students)

    print("Topper:", stats["topper"])

    print("Pass percentage:", stats["pass_percentage"])

    print("Subject averages:", stats["subject_averages"])

    stats_selected = class_statistics(
        students, "Python", "Stats"
    )

    print(
        "Python and Stats only:",
        stats_selected["subject_averages"]
    )

# Calling Main Function
if __name__ == "__main__":
    main()