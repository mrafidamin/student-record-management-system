from students_data import students
from functions import *

# Display command menu once at first
print("Welcome to Student Record Management")
print("1. View All Students")
print("2. Search Student")
print("3. Add Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Count Students")
print("7. Highest, Lowest & Average CGPA")
print("8. Students Above Average")
print("9. Students Below 3.00")
print("10. Top 3 Students")
print("11. Sort by Name")
print("12. Sort by Age")
print("13. Sort by CGPA")
print("14. Search by Name")
print("15. Find Student with Initial Letter")
print("16. Exit")

# Interacting options using while loop
while True:
    try:
        option = int(input("Please select an option: "))
    except ValueError:
        print("Please enter a valid number.")
    # 1. View All Students
    if option == 1: 
        view_students()

    # 2. Search Student
    elif option == 2: 
        search_by_id()

    # 3. Add Student
    elif option == 3: 
        add_student()

    # 4. Update Student
    elif option == 4: 
        update_info()

    # 5. Delete Student
    elif option == 5: 
        delete_student()

    # 6. Count Students
    elif option == 6: 
        count_students()

    # 7. Highest, Lowest & Average CGPA
    elif option == 7: 
        cgpa_stats()

    # 8. Students Above Average CGPA
    elif option == 8: 
        filter_above_average()

    # 9. Students Below CGPA of 3.00
    elif option == 9: 
        filter_below_three()

    # 10. Top Three Students
    elif option == 10: 
        filter_top_three()

    # 11. Sort by Name
    elif option == 11: 
        sort_by_name()

    # 12. Sort by Age
    elif option == 12: 
        sort_by_age()

    # 13. Sort by CGPA
    elif option == 13: 
        sort_by_cgpa()

    # 14. Search by Name
    elif option == 14: 
        search_by_name()

    # 15. Find Student with Initial Letter
    elif option == 15: 
        find_with_initial()

    # 16. Exit
    elif option == 16: 
        print("Thank you for using the Student Record Management System!")
        break
    else:
        print("Invalid option. Please try again.")

