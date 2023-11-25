import os


def clear_screen():
    _ = os.system("cls")


database = []


def add():
    name = input("Enter Name: ")
    age = int(input("Enter age: "))
    id = input("Enter ID: ")
    grade = int(input("Enter grade: "))
    student = {"name": name, "age": age, "id": id, "grade": grade}
    database.append(student)


def search():
    name = input("Enter name of studnet you want to search: ")
    for student in database:
        if student["name"] == name:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Grade:", student["grade"])
            break
    else:
        print("Student not found.")


def list_all():
    if not database:
        print("No students in the database.")
        return

    for student in database:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grade:", student["grade"])
        print()


def update_student():
    name = input("Enter student name: ")

    for student in database:
        if student["name"] == name:
            print("Found student:", student["name"])
            student["name"] = input(
                "Enter updated name (leave blank to keep current): "
            )
            student["age"] = input("Enter updated age (leave blank to keep current): ")
            student["grade"] = input(
                "Enter updated grade (leave blank to keep current): "
            )

            print("Student updated successfully.")
            break
    else:
        print("Student not found.")


def delete_student():
    name = input("Enter student name: ")

    for student in database:
        if student["name"] == name:
            database.remove(student)
            print("Student deleted successfully.")
            break
    else:
        print("Student not found.")


while True:
    print()
    print()
    print("===================================")
    print("Student Database ")
    print("what you can do here")
    choise = int(
        input(
            "Enter 1 to add student \n Enter 2 to view student \n Enter 3 to list all students \n Enter 4 to update \n Enter 5 to Delete \n Enter 0 to exit\n"
        )
    )

    if choise == 1:
        clear_screen()
        print("Add Studnet ")
        add()
        print("Student Added!!")

    elif choise == 2:
        clear_screen()
        print("Search Student ")
        search()
    elif choise == 3:
        clear_screen()
        print("list all Students ")
        list_all()

    elif choise == 4:
        clear_screen()
        print("Update Student ")
        update_student()
    elif choise == 5:
        clear_screen()
        print("Delete Student")
        delete_student()
    elif choise == 0:
        break
