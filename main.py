from student import add_student, view_students, search_student, delete_student
from file_handaler import load_students, save_students

def menu():
    print("""
===== Student Management System =====
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
""")

def main():
    students = load_students()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
            save_students(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            delete_student(students)
            save_students(students)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
