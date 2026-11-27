# 🎓 Student Record Management System
### 📊 Student Performance Analytics & Data Visualization

<p align="center">
  <img src="https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-Data%20Visualization-11557c" />
  <img src="https://img.shields.io/badge/Storage-CSV-orange" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

## 📌 Project Overview

The **Student Record Management System** is a Python-based console application designed to manage student information and analyze academic performance.

The application provides essential student management operations such as adding, viewing, searching, updating, and deleting student records.

It uses **CSV (Comma-Separated Values)** files for permanent data storage and integrates **NumPy, Pandas, and Matplotlib** to perform statistical calculations, analyze student performance, and generate graphical reports.

This project demonstrates the practical implementation of Python programming concepts, data structures, data analysis, and visualization.

---

## 🎯 Project Objectives

- 📂 Maintain student records efficiently.
- ➕ Add new student information.
- 🔍 Search students using unique roll numbers.
- ✏️ Update existing student marks.
- 🗑️ Delete student records.
- 📊 Calculate student performance statistics.
- 📈 Analyze course-wise academic performance.
- 📉 Generate graphical representations of student data.
- 💾 Store records permanently using CSV files.

---

## ✨ Key Features

### 👨‍🎓 Student Management (CRUD)

| Feature | Description |
|---|---|
| ➕ Add Student | Register a new student record. |
| 📋 View Students | Display all student records in table format. |
| 🔍 Search Student | Find students using their roll number. |
| ✏️ Update Student | Update existing student marks. |
| 🗑️ Delete Student | Remove student records from the system. |

### 📊 Student Performance Analytics

- Calculate total number of students.
- Calculate average marks.
- Identify highest and lowest marks.
- Calculate median marks.
- Calculate standard deviation.
- Count students scoring above 75.
- Count students scoring below 40.
- Generate course-wise performance reports.

### 📈 Data Visualization

The project generates three graphical reports using Matplotlib:

| Chart | Description |
|---|---|
| 📊 Student Marks Comparison | Compares marks obtained by individual students. |
| 📉 Marks Distribution | Displays the distribution of student marks. |
| 🥧 Course Distribution | Displays the percentage of students in different courses. |

### 📄 Automatic Report Generation

The application automatically generates these reports inside `codebase/outputs/`:

- `performance_summary.csv`
- `course_wise_performance.csv`

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python 3 | Core programming language |
| 🔢 NumPy | Numerical calculations and statistical operations |
| 🐼 Pandas | Data processing and analysis |
| 📊 Matplotlib | Graphical data visualization |
| 📁 CSV Module | Reading and writing student records |
| 🧮 Lists | Managing multiple student records |
| 🔑 Dictionaries | Student record indexing and searching |
| 📦 Tuples | Structured student record representation |
| 💻 VS Code | Development environment |
| 🐙 Git & GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
Student-Record-Management-System/
│
├── 📂 codebase/\n│   ├── 📄 student_record_management.py\n│   ├── 📂 data/\n│   │   └── 📄 students.csv\n│   └── 📂 outputs/\n│       ├── 📊 student_marks.png\n│       ├── 📊 marks_distribution.png\n│       ├── 🥧 course_distribution.png\n│       ├── 📄 performance_summary.csv\n│       └── 📄 course_wise_performance.csv
│
├── 📂 data/
│   └── 📄 students.csv
│
├── 📂 outputs/
│   ├── 📊 student_marks.png
│   ├── 📊 marks_distribution.png
│   ├── 🥧 course_distribution.png
│   ├── 📄 performance_summary.csv
│   └── 📄 course_wise_performance.csv
│
├── 📂 screenshots/
│
├── 📄 README.md
│
└── 📄 .gitignore
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project on your local machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/himanshuyadaaav/Student-Record-Management-System.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Student-Record-Management-System
```

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python codebase/student_record_management.py
```

---

## 🖥️ Application Menu

When the application starts, the following menu is displayed:

```text
=============================================================
          STUDENT RECORD MANAGEMENT SYSTEM
              & PERFORMANCE ANALYTICS
=============================================================

STUDENT MANAGEMENT

1. Add Student
2. View All Students
3. Search Student
4. Update Student Marks
5. Delete Student

STUDENT ANALYTICS

6. Student Performance Summary
7. Course-wise Performance

PROJECT OUTPUTS

8. Generate All Project Outputs

9. Exit

=============================================================
Enter Your Choice:
```

---

## 💾 CSV Database Structure

The project uses `students.csv` as its primary data storage file.

### 📄 File: `codebase/data/students.csv`

| Column | Description | Data Type |
|---|---|---|
| `roll_no` | Unique student roll number | String |
| `name` | Student full name | String |
| `course` | Student enrolled course | String |
| `marks` | Student obtained marks | Integer |

### Example CSV Data

```csv
roll_no,name,course,marks
101,Aman Sharma,BTech,78
102,Riya Verma,BTech,100
103,Neha Singh,BCA,85
104,Ravi Kumar,BCA,90
105,Priya Gupta,BCA,65
106,Rahul Yadav,BTech,45
107,Anjali Das,BCA,92
108,Arjun Patel,BTech,35
```

✅ Student records are stored permanently in the CSV file.

✅ Changes made through Add, Update, and Delete operations are saved automatically.

✅ Records are loaded again when the application restarts.

---

## 📊 Generated Project Outputs

After selecting **Option 8 – Generate All Project Outputs**, the application creates the following files inside the `codebase/outputs` directory.

### 🖼️ Graphical Reports

| File Name | Output |
|---|---|
| `student_marks.png` | Student Marks Comparison Chart |
| `marks_distribution.png` | Student Marks Distribution Histogram |
| `course_distribution.png` | Course Distribution Pie Chart |

### 📄 Analytical Reports

| File Name | Output |
|---|---|
| `performance_summary.csv` | Overall Student Performance Statistics |
| `course_wise_performance.csv` | Course-wise Performance Analysis |

All reports are generated using the latest records available in `codebase/data/students.csv`.

---

## ✅ Data Validation

The system includes validation to maintain data accuracy and consistency.

| Validation | Expected Behaviour |
|---|---|
| Duplicate Roll Number | Prevents duplicate student records. |
| Empty Roll Number | Displays validation error. |
| Empty Student Name | Displays validation error. |
| Empty Course | Displays validation error. |
| Marks Below 0 | Rejects invalid marks. |
| Marks Above 100 | Rejects invalid marks. |
| Invalid Marks Input | Handles non-numeric input. |
| Student Not Found | Displays an appropriate error message. |

---

## 📚 Python Syllabus Concepts Implemented

This project demonstrates practical applications of concepts covered in the Python programming syllabus.

| Unit | Concepts | Implementation |
|---|---|---|
| Unit 1 | Computational Thinking, Algorithm, Flowchart, Pseudocode | Project planning and algorithm design |
| Unit 2 | Variables, Conditions, Loops, Lists, Tuples, Dictionaries, Functions, Exception Handling | Student record management |
| Unit 3 | NumPy Arrays, Indexing, Statistical Operations | Student marks analysis |
| Unit 4 | Pandas Series, DataFrames, CSV, Data Cleaning | Data processing and report generation |
| Unit 5 | Matplotlib, Bar Charts, Histograms, Pie Charts | Student performance visualization |

---

## 🔐 Data Storage Architecture

The application follows a simple layered architecture.

```text
              👨‍🎓 USER
                 |
                 ▼
          🖥️ CONSOLE MENU
                 |
                 ▼
         ⚙️ APPLICATION LOGIC
                 |
                 ▼
          ✅ VALIDATION LAYER
                 |
                 ▼
          📦 DATA STRUCTURES
          /       |        \
       Lists    Tuples  Dictionaries
                 |
                 ▼
           📁 CSV STORAGE
                 |
                 ▼
           🐼 PANDAS
                 |
                 ▼
             🔢 NumPy
                 |
                 ▼
           📊 Matplotlib
                 |
                 ▼
          📂 OUTPUT REPORTS
```

---

## 🚀 Future Enhancements

The project can be extended with additional functionality in the future:

- 🌐 Web-based student management interface.
- 🔐 Admin login and authentication.
- 📚 Subject-wise student marks.
- 🏆 Automatic grade calculation.
- 📑 PDF report generation.
- 📊 Advanced academic performance analytics.
- 🔎 Advanced student filtering and sorting.
- 🗄️ Integration with SQLite or MySQL databases.

---

## ⚠️ Project Limitations

- The application currently uses a command-line interface.
- CSV is used for storage instead of a dedicated database.
- The system currently supports updating student marks rather than all student details.
- The application does not include user authentication.

---

## 🎓 Project Information

| Detail | Information |
|---|---|
| Project Title | Student Record Management System |
| Problem Statement Number | PS No. 18 |
| Programming Language | Python 3 |
| Application Type | Console-Based Application |
| Data Storage | CSV File |
| Data Analysis | NumPy & Pandas |
| Visualization | Matplotlib |
| Project Category | Academic Python Project |

---

## 👨‍💻 Author

**Developed as an academic project using Python programming.**

---

## ⭐ Support

If you find this project useful, consider giving this repository a ⭐ on GitHub!

**Thank you for visiting this project!** 🚀
