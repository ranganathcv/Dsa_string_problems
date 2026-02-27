def student(name):
    students={"Alice":98,"Bob":86,"Ranga":81,"Siri":100,"Hamsa":93}
    if name in students:
        print(f"{name}'s marks are:{students[name]}")
    else:
        print("Student not found")

name=input("Enter the student's name :")
student(name)