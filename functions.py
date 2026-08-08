from students_data import students

# View all students
def view_students():
    for id, info in students.items():
        print(f"{id} | {info['name']} | Age: {info['age']} | CGPA: {info['cgpa']}")

# Search by ID
def search_by_id():
    student_id = input("Please enter an ID number to search: ").upper()
    if student_id in students:
        student = students[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"CGPA: {student['cgpa']}")

# Add new student
def add_student():
    new_student_id = input("Enter new student ID: ").upper()
    if new_student_id in students:
        print("ID already exists.")
    else:
        name = input("Enter full name: ")
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Age must be an integer number.")
        
        try:
            cgpa = float(input("Enter CGPA: "))
        except ValueError:
            print("CGPA must be a float number.")
        

        students[new_student_id] = {
            'name': name,
            'age': age,
            'cgpa': cgpa
        }

        print("Student name added successfully!")

# Update information
def update_info():
    id_for_update = input("Enter student ID for update: ").upper()
    if id_for_update in students:
        name = input("Enter updated name: ")
        
        try:
            age = int(input("Enter updated age: "))
            cgpa = float(input("Enter updated CGPA: "))

        except ValueError:
            print("Age must be an integer and CGPA must be a float.")

        students[id_for_update]['name'] = name
        students[id_for_update]['age'] = age
        students[id_for_update]['cgpa'] = cgpa

        print("Student information updated succesfully.")
    else:
        print("Student ID not found.")

# Delete student
def delete_student():
    id_for_delete = input("Enter ID for delete: ")
    if id_for_delete in students:
        del students[id_for_delete]
    else:
        print("ID not found.")

# Count students
def count_students():
    print(f"Total Students: {len(students)}")

# List of CGPA
cgpa_list = []

for student in students.values():
    cgpa_list.append(student['cgpa'])

# Highest, lowest, and average CGPA
def cgpa_stats():
    try:
        highest_cgpa = max(cgpa_list)
        lowest_cgpa = min(cgpa_list)
        average_cgpa = sum(cgpa_list) / len(cgpa_list)
    except ValueError:
        print("No student CGPA available.")
    
    print(f"Highest CGPA: {highest_cgpa}")
    print(f"Lowest CGPA: {lowest_cgpa}")
    print(f"Average CGPA: {average_cgpa}")

    return average_cgpa

# Students above average
def filter_above_average():
    average_cgpa = cgpa_stats()
    print("Students with CGPA above average:")
    for student in students.values():
        if student['cgpa'] > average_cgpa:
            print(f"{student['name']}")

# Students below 3.00 CGPA
def filter_below_three():
    print("Students below 3.00 CGPA")
    for student in students.values():
        if student['cgpa'] < 3.00:
            print(f"{student['name']}")

# Sort students by name (A–Z)
def sort_by_name():
    sorted_by_name = sorted(
        students.items(),
        key = lambda x: x[1]['name']
    )
    print("Students sorted A-Z")
    for id, info in sorted_by_name:
        print(f"{id}, {info['name']}, Age: {info['age']}, CGPA: {info['cgpa']}")

# Sort students by age (Youngest → Oldest)
def sort_by_age():
    sorted_by_age = sorted(
        students.items(),
        key = lambda x: x[1]['age']
    )
    print("Students sorted by age (Youngest → Oldest)")
    for id, info in sorted_by_age:
        print(f"{id}, {info['name']}, Age: {info['age']}, CGPA: {info['cgpa']}")

# Sort students by CGPA (Highest → Lowest)
def sort_by_cgpa():
    sorted_by_cgpa = sorted(
        students.items(),
        key = lambda x : x[1]['cgpa'],
        reverse=True
    )
    print("Students sorted into CGPA")
    for id, info in sorted_by_cgpa:
        print(f"{id}, {info['name']}, Age: {info['age']}, CGPA: {info['cgpa']}")
    return sorted_by_cgpa
    
# Display top three students
def filter_top_three():
    sorted_by_cgpa = sort_by_cgpa()
    print("Top 3 students")
    for id, info in sorted_by_cgpa[:3]:
        print(f"{info['name']}")

# Search students by name (allow user to enter part of a name)
def search_by_name():
    search_name = input("Enter a name to search: ").lower()
    found = False
    print("Search result:")
    for student in students.values():
        if search_name in student['name'].lower():
            print(f"{student['name']}")
            found = True
    if not found:
        print(f"{search_name} not found.")

# Find student with initial letter
def find_with_initial():
    initial_found = False
    initial = input("Enter a letter: ")
    for student in students.values():
        if initial.lower() == student['name'][0].lower():
            initial_found = True
            print(f"{student['name']}")
    if not initial_found:
        print(f"No student found with initial {initial}")
