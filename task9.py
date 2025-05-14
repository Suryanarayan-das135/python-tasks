# Create a Dictionary of Student Marks

student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

#Ask the user to input a student's name
name = input("Enter the student's name: ")

# display marks or show error message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student named '{name}' not found.")
