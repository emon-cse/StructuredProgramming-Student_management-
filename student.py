def add_student(students):
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")

    students.append({
        "id": id,
        "name": name,
        "age": age,
        "grade": grade
    })
    print("Student added successfully")


def view_students(students):
    if not students:
        print("No students found")
        return

    print("\nID | Name | Age | Grade")
    print("-" * 25)
    for s in students:
        print(f"{s['id']} | {s['name']} | {s['age']} | {s['grade']}")


def search_student(students):
    search_id = input("Enter student ID to search: ")
    for s in students:
        if s["id"] == search_id:
            print("Student Found:", s)
            return
    print("Student not found.")


def delete_student(students):
    delete_id = input("Enter student ID to delete: ")
    for s in students:
        if s["id"] == delete_id:
            students.remove(s)
            print("🗑 Student deleted.")
            return
    print("Student not found.")
