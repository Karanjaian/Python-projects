def add_students():
    students = {}
    num = int(input("Enter number of students: "))

    for _ in range(num):
        name = input("Enter student name: ")
        score = float(input(f"Enter {name}'s score: "))
        students[name] = score
    return students

def show_results(students):
    print("\n--- Student Results ---")
    total = 0
    for name, score in students.items():
        status = "Pass" if score >= 50 else "Fail"
        print(f"{name}: {score} - {status}")
        total += score

    average = total / len(students)
    print(f"\nClass Average: {average:.2f}")

print("Welcome to the Student Grade Manager!")
students = add_students()
show_results(students)
