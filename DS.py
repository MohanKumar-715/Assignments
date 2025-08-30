students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 92,
    "Eva": 88
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found in the records.")
