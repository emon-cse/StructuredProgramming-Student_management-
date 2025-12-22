import os
BASE_DIR = r"D:\New Folder\Learning\Software Development\Folder\Structured Programming project"
DATA_FILE = os.path.join(BASE_DIR, "data.txt")


def load_students():
    students = []
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                id, name, age, grade = line.strip().split(",")
                students.append({
                    "id": id,
                    "name": name,
                    "age": age,
                    "grade": grade
                })
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    with open(DATA_FILE, "w") as file:
        for s in students:
            file.write(f"{s['id']},{s['name']},{s['age']},{s['grade']}\n")
