import json

def display_menu():
    print(f"Welcome to mechatronics departmental portal !")
    print("1. Add a new student")
    print("2. Input semester grade")
    print("3. View student Record")
    print("4. Update students grades")
    print("5. Calculate GPA for a student")
    print("6. Calculate CGPA for a  student")
    print("7. View all registered students")
    print("8. Exit")


### Function to get the grade point system based on student scores ###
def get_grade_point(score):
        if score >= 70 and score <=100:
            return 5.0
        elif score >= 60 and score <= 69:
            return 4.0
        elif score >= 50 and score <= 59:
            return 3.0
        elif score >= 45 and score <= 49:
            return 2.0
        elif score >= 40 and score <= 44:
            return 1.0
        else:
            return 0.0
### Courses with credit unit ###        
Course_list = {
    1: {
        "MTH 101" : 3,
        "PHY 101" : 3,
        "CHM 101" : 3,
        "GST 101" : 2,
        "CSC 101" : 2,
        "GST 103" : 2,
        "GST 105" : 2,
        "GET 111" : 2,
        "GST 107" : 2,
        "PHY 107" : 1,
        "CHM 107" : 1,
    },
    2: {
        "MTH 102" : 3,
        "PHY 102" : 3,
        "CHM 102" : 3,
        "GST 102" : 2,
        "GST 104" : 2,
        "GST 106" : 2,
        "STA 102" : 2,
        "AED 101" : 1,
        "PHY 108" : 1,
        "CHM 108" : 1,
    },
    3:{
        "GST 201" : 2,
        "GST 203" : 2,
        "GET 201" : 3,
        "GET 203" : 2,
        "GET 205" : 3,
        "GET 207" : 3,
        "GET 209" : 3,
        "GET 211" : 3,
        "GET 213" : 1,
    },
    4:{
        "GET 202" : 2,
        "GET 204" : 2,
        "GET 206" : 3,
        "GET 208" : 3,
        "GET 210" : 3,
        "GET 212" : 2,
        "GET 222" : 2,
        "GST 202" : 2,
        "GST 224" : 2,
        "GET 229" : 2,
    },
    5:{
        "GET 301" : 3,
        "GET 303" : 2,
        "GST 311" : 2,
        "MCT 301" : 3,
        "MCT 303" : 2,
        "MCT 305" : 3,
        "MCT 307" : 2,
        "MCT 309" : 3,
        "MCT 311" : 2,
        "MCT 313" : 2,
        "MEE 331" : 2,
    },
    6:{
        "GET 302" : 3,
        "GET 304" : 2,
        "GET 399" : 2,
        "MCT 302" : 3,
        "MCT 304" : 2,
        "MCT 306" : 3,
        "MCT 308" : 3,
        "MCT 310" : 2,
        "MCT 312" : 2,
        "MCT 314" : 2,
    },
    7:{
        "MCT 401" : 3,
        "MCT 403" : 2,
        "MCT 405" : 2,
        "MCT 407" : 2,
        "MCT 409" : 3,
        "MCT 411" : 3,
        "MCT 413" : 2,
        "MCT 415" : 2,
        "MCT 423" : 1,
        "MCT 425" : 1,

    },
    8:{
        "MCT 499" : 6,
    },
    9:{
        "GET 501" : 3,
        "MCT 501" : 2,
        "MCT 503" : 3,
        "MCT 505" : 3,
        "MCT 507" : 2,
        "MCT 509" : 2,
        "MCT 511" : 2,
        "MCT 513" : 2,
        "MCT 517" : 2,
        "MCT 519" : 2,
        "MCT 521" : 2,
        "MCT 523" : 2,
    },
    10:{
        "GET 502" : 2,
        "MCT 502" : 2,
        "MCT 504" : 3,
        "MCT 506" : 2,
        "MCT 512" : 2,
        "MCT 514" : 1,
        "MCT 516" : 1,
        "MCT 522" : 1,
        "MCT 524" : 1,
        "MCT 526" : 1,
        "MCT 528" : 1,
        "MCT 530" : 1,
    },

}

###
def add_students(students):
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student ID already exist")
    else:
        name = input("Enter student name: ")
        students[student_id] = {
            "name" : name,
            "semesters" : {}
        }
        print(f"student {name} sucessfully added")

def view_all_students(students):
    if not students:
        print("No students found yet")
        return
    print("All registered students")
    for student_id, data in students.items():
        name = data["name"]
        semester_count = len (data["semesters"])
        print(f"ID: {student_id} | Name: {name} | Semesters Recorded: {semester_count}")


def display_students(students):
    if not students:
        print("Student data is empty.")
        return
    print("All Registered Students")
    for student_id, student_info in students.items():
        print(f"ID: {student_id}, Name: {student_info['name']}")
        if not student_info["semesters"]:
            print("  No semesters recorded.")
        else:
            for semester, courses in student_info["semesters"].items():
                print(f"  Semester {semester}:")
                for course, score in courses.items():
                    print(f"    {course}: {score}")

def input_semester_grades(students):
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student Not Found.")
        return
    

    try:
        semester = int(input("Enter semester (1 - 10):"))
        if semester < 1 or semester > 10:
            print("Semester must be between 1 and 10")
            return
    except ValueError:
        print("Invalid semester")
        return
    
    students[student_id]["semesters"][semester] = {}

    for course, unit in Course_list.items():
        while True:
            try:
                score = float (input(f"Enter score for {course} (CU:{unit}): "))
                if 0 <= score <= 100:
                    students[student_id]["semesters"][semester][course] = score
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    print(f"Grades recorded for semester {semester}.")

## save students data to a json file ##
def save_students(students, filename= "students_data.json"):
    with open(filename, "w") as f:
        json.dump(students, f, indent=4)
    print("Student data saved successfully.")

def load_students(filename="students_data.json"):
    try:
        with open(filename, "r") as f:
            students = json.load(f)
        print("student data successfully saved.")
        return students
    except FileNotFoundError:
        print("Data not found.")
        return{}
    

def view_student_records(students):
    student_id  =(input("Enter student ID:"))
    if student_id not in students:
        print("Students not found.")
        return
    
    student = students[student_id]
    print(f"Student: {student['name']}")

    if not student["semesters"]:
        print("No semester recorded at the moment.")
        return
    for semester, courses in student["semesters"].items():
        print(f"Semester {semester}:")
        for course, score in courses.items():
            print(f"  {course}: {score}")
    
def update_grade(students):
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found.")
        return

    try:
        semester = int(input("Enter semester number (1-10): "))
    except ValueError:
        print("Invalid semester number.")
        return

    if semester not in students[student_id]["semesters"]:
        print("No grades recorded for this semester yet.")
        return

    course = input("Enter course code to update: ")
    if course not in students[student_id]["semesters"][semester]:
        print("Course not found for this semester.")
        return

    while True:
        try:
            new_score = float(input(f"Enter new score for {course}: "))
            if 0 <= new_score <= 100:
                students[student_id]["semesters"][semester][course] = new_score
                print(f"Score for {course} in semester {semester} updated to {new_score}.")
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
def calculate_gpa(students):
      student_id = input("Enter student ID: ")
      if student_id not in students:
        print("Student not found.")
        return

      try:
        semester = int(input("Enter semester number (1-10): "))
      except ValueError:
        print("Invalid semester number.")
        return

      if semester not in students[student_id]["semesters"]:
        print("No grades recorded for this semester yet.")
        return

      courses = students[student_id]["semesters"][semester]

      total_points = 0
      total_units = 0

      for course, score in courses.items():
          unit = Course_list[course]
          grade_point = get_grade_point(score)
          total_points += grade_point * unit
          total_units += unit

      if total_units == 0:
         print("No credit units found. GPA cannot be calculated.")
         return

      gpa = total_points / total_units
      print(f"GPA for semester {semester}: {gpa: }")

def calculate_cgpa(students):
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("student not found.")
        return
    
    try:
        latest_semester =int(input("Calculate CGPA up to which semester(1-10)?: "))
    except ValueError:
        print("Invalid semester number.")
        return
    
    student = students[student_id]
    total_points = 0
    total_units = 0

    for semester in range(1, latest_semester + 1):
        if semester in student["semesters"]:
            Course_list = student["semesters"][semester]
            for course, score in Course_list.items():
                unit = Course_list(course)
                grade_point = get_grade_point(score)
                total_points = total_points + grade_point * unit
                total_units = total_units + unit

    if total_units == 0:
        print("The current credit units is 0, CGPA not calculated")
        return

    cgpa = total_points / total_units
    print(f"Your current CGPA up to {latest_semester}: is {cgpa}")



    
def main():
    students = load_students()
    students = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-8): ")

        if choice == '1':
            add_students(students)
            
        elif choice == '2':
            input_semester_grades(students)
            save_students(students)
        elif choice == '3':
            view_student_records(students)
        elif choice == '4':
            update_grade(students)
            save_students(students)
        elif choice == '5':
            calculate_gpa(students)
        elif choice == '6':
            calculate_cgpa(students)
        elif choice == '7':
            view_all_students(students)
        elif choice == '8':
            save_students(students)
            print("Exiting Exam Officer System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
        
