import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
CSV_FILE = DATA_DIR / "students.csv"

FIELDNAMES = ["roll_no", "name", "course", "marks"]


def initialize_csv():

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:

        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_students():

    students = []

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            row["marks"] = int(row["marks"])
            students.append(row)

    return students


def save_students(students):

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        writer.writeheader()
        writer.writerows(students)


def load_dataframe():

    return pd.read_csv(CSV_FILE)


def create_student_index(students):

    student_index = {
        student["roll_no"]: student
        for student in students
    }

    return student_index


def validate_marks():

    try:

        marks = int(input("Enter Marks (0-100): "))

        if 0 <= marks <= 100:
            return marks

        print("Marks must be between 0 and 100.")

    except ValueError:

        print("Please enter valid numeric marks.")

    return None


def display_table(students):

    if not students:
        print("No student records found.")
        return

    print("\n" + "=" * 70)
    print(f"{'Roll No':<12}{'Name':<22}{'Course':<16}{'Marks':<10}")
    print("=" * 70)

    for student in students:

        student_tuple = (
            student["roll_no"],
            student["name"],
            student["course"],
            student["marks"]
        )

        roll, name, course, marks = student_tuple

        print(f"{roll:<12}{name:<22}{course:<16}{marks:<10}")

    print("=" * 70)


def add_student():

    students = load_students()
    student_index = create_student_index(students)

    print("\n---------- ADD STUDENT ----------")

    roll_no = input("Enter Roll Number: ").strip()

    if not roll_no:
        print("Roll number cannot be empty.")
        return

    if roll_no in student_index:
        print(f"Roll number {roll_no} already exists.")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    course = input("Enter Course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    marks = validate_marks()

    if marks is None:
        return

    new_student = {
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(new_student)

    save_students(students)

    print(f"Record added: {roll_no} | {name} | {course} | {marks}")


def view_students():

    students = load_students()

    print("\n---------- ALL STUDENTS ----------")

    display_table(students)


def search_student():

    students = load_students()
    student_index = create_student_index(students)

    print("\n---------- SEARCH STUDENT ----------")

    roll_no = input("Enter Roll Number: ").strip()

    student = student_index.get(roll_no)

    if student:
        display_table([student])
    else:
        print(f"Roll number {roll_no} not found.")


def update_student():

    students = load_students()
    student_index = create_student_index(students)

    print("\n---------- UPDATE STUDENT ----------")

    roll_no = input("Enter Roll Number: ").strip()

    student = student_index.get(roll_no)

    if student is None:
        print(f"Roll number {roll_no} not found.")
        return

    print("Student Name:", student["name"])
    print("Current Marks:", student["marks"])

    print("\nEnter New Marks:")

    new_marks = validate_marks()

    if new_marks is None:
        return

    student["marks"] = new_marks

    save_students(students)

    print(f"Marks updated: {new_marks}")


def delete_student():

    students = load_students()
    student_index = create_student_index(students)

    print("\n---------- DELETE STUDENT ----------")

    roll_no = input("Enter Roll Number: ").strip()

    if roll_no not in student_index:
        print(f"Roll number {roll_no} not found.")
        return

    students = [
        student for student in students
        if student["roll_no"] != roll_no
    ]

    save_students(students)

    print(f"Student record {roll_no} deleted successfully.")


def performance_summary():

    df = load_dataframe()

    if df.empty:
        print("No student records available.")
        return

    marks_array = df["marks"].to_numpy(dtype=float)

    print("\n========== STUDENT PERFORMANCE SUMMARY ==========")

    print("Total Students:", len(df))
    print("Average Marks:", round(np.mean(marks_array), 2))
    print("Highest Marks:", np.max(marks_array))
    print("Lowest Marks:", np.min(marks_array))
    print("Median Marks:", np.median(marks_array))
    print("Standard Deviation:", round(np.std(marks_array), 2))
    print("Students Above 75:", np.sum(marks_array > 75))
    print("Students Below 40:", np.sum(marks_array < 40))

    print("\n========== PANDAS STATISTICS ==========")

    print(df["marks"].describe().round(2))


def course_wise_performance():

    df = load_dataframe()

    if df.empty:
        print("No student records available.")
        return

    print("\n========== COURSE-WISE PERFORMANCE ==========")

    summary = df.groupby("course").agg(
        total_students=("roll_no", "count"),
        average_marks=("marks", "mean"),
        highest_marks=("marks", "max"),
        lowest_marks=("marks", "min")
    ).reset_index()

    summary["average_marks"] = summary["average_marks"].round(2)

    print(summary.to_string(index=False))


def student_marks_chart():

    df = load_dataframe()

    if df.empty:
        print("No student records available.")
        return

    plt.figure(figsize=(11, 6))

    plt.bar(df["name"], df["marks"])

    plt.xlabel("Student Name")
    plt.ylabel("Marks")
    plt.title("Student Marks Comparison")

    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 110)

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "student_marks.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("Student marks chart generated successfully.")


def marks_distribution_chart():

    df = load_dataframe()

    if df.empty:
        print("No student records available.")
        return

    plt.figure(figsize=(9, 6))

    plt.hist(
        df["marks"],
        bins=10,
        range=(0, 100),
        edgecolor="black"
    )

    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.title("Student Marks Distribution")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "marks_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("Marks distribution chart generated successfully.")


def course_distribution_chart():

    df = load_dataframe()

    if df.empty:
        print("No student records available.")
        return

    course_counts = df["course"].value_counts()

    plt.figure(figsize=(8, 8))

    plt.pie(
        course_counts,
        labels=course_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Student Course Distribution")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "course_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("Course distribution chart generated successfully.")


def export_performance_report():

    df = load_dataframe()

    if df.empty:
        print("No student records available.")
        return

    marks = df["marks"].to_numpy(dtype=float)

    summary = pd.DataFrame([{
        "total_students": len(df),
        "average_marks": round(np.mean(marks), 2),
        "highest_marks": np.max(marks),
        "lowest_marks": np.min(marks),
        "median_marks": np.median(marks),
        "standard_deviation": round(np.std(marks), 2),
        "students_above_75": int(np.sum(marks > 75)),
        "students_below_40": int(np.sum(marks < 40))
    }])

    summary.to_csv(
        OUTPUT_DIR / "performance_summary.csv",
        index=False
    )

    print("Performance summary exported successfully.")


def export_course_report():

    df = load_dataframe()

    if df.empty:
        print("No student records available.")
        return

    summary = df.groupby("course").agg(
        total_students=("roll_no", "count"),
        average_marks=("marks", "mean"),
        highest_marks=("marks", "max"),
        lowest_marks=("marks", "min")
    ).reset_index()

    summary["average_marks"] = summary["average_marks"].round(2)

    summary.to_csv(
        OUTPUT_DIR / "course_wise_performance.csv",
        index=False
    )

    print("Course-wise report exported successfully.")


def generate_all_outputs():

    df = load_dataframe()

    if df.empty:
        print("No student records available to generate outputs.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("\n========== GENERATING PROJECT OUTPUTS ==========")

    student_marks_chart()
    marks_distribution_chart()
    course_distribution_chart()

    export_performance_report()
    export_course_report()

    print("\n==============================================")
    print("ALL PROJECT OUTPUTS GENERATED SUCCESSFULLY")
    print("==============================================")

    print("\nOutput Files:")

    output_files = [
        "student_marks.png",
        "marks_distribution.png",
        "course_distribution.png",
        "performance_summary.csv",
        "course_wise_performance.csv"
    ]

    for file_name in output_files:
        print("->", file_name)

    print("\nOutput Folder:", OUTPUT_DIR)


def main():

    initialize_csv()

    while True:

        print("\n")
        print("=" * 65)
        print("          STUDENT RECORD MANAGEMENT SYSTEM")
        print("              & PERFORMANCE ANALYTICS")
        print("=" * 65)

        print("\nSTUDENT MANAGEMENT")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")

        print("\nSTUDENT ANALYTICS")

        print("6. Student Performance Summary")
        print("7. Course-wise Performance")

        print("\nPROJECT OUTPUTS")

        print("8. Generate All Project Outputs")

        print("\n9. Exit")

        print("=" * 65)

        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            performance_summary()

        elif choice == "7":
            course_wise_performance()

        elif choice == "8":
            generate_all_outputs()

        elif choice == "9":
            print("\nThank you for using Student Record Management System!")
            break

        else:
            print("Invalid choice! Please select 1-9.")


if __name__ == "__main__":
    main()