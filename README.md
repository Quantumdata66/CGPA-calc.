# 🎓 University CGPA Calculator (Mechatronics Dept)

This is a simple **Python-based GPA & CGPA calculator** designed to help a university exam officer manage student results for up to **10 semesters**, using a real Nigerian university grading system.



##  Features

* 📚 Add new students
* ✏️ Enter semester results for multiple courses
* 🗂️ Store results persistently using JSON
* 🔢 Automatically calculate GPA and CGPA
* 🔄 Update results for multiple semesters
* 📋 View all registered students and their details

# ⚙️ How it works

### The program covers: ###
**Python fundamentals** which includes variables, data types, loops, functions, conditionals
**Dictionaries & lists** to store courses, scores & credit units
**JSON file storage** so data is saved locally
It’s currently a **command-line program** you run in your terminal.
The next version will be a **web app (Flask)** so exam officers can use it remotely, (comming very soon)

## GPA & CGPA Calculation

Each course has a **credit unit (CU)**.
Student scores are converted to **grade points** based on the Nigerian scale:
* 70–100 → 5.0 (A)
* 60–69 → 4.0 (B)
* 50–59 → 3.0 (C)
* 45–49 → 2.0 (D)
* 40–44 → 1.0 (E)
*  0–39 → 0.0 (F)
**GPA** is calculated for each semester:  
* A grade (A, B, C, D, E, F)
* A grade point (usually: A = 5, B = 4, C = 3, D = 2, E = 1, F = 0)
* A credit unit (CU) (the course weight, e.g. 2, 3, or 4 units) 
   The grade point of each course multiply by the credit unit for the individual course, it is then summed and divided by the total credit unit for the semester.

**CGPA** is the cumulative average across all semesters.
  CGPA is the average of all your GPAs from all semesters up to your current level, The total grade point for all semester divided by the total credit unit for all semester
