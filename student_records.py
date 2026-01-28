# student_records.py
# Dictionary and JSON demonstration

import json   # Used to work with JSON data

# -------- Dictionary to store student details --------
students = {
    "101": {"name": "Aman", "age": 20, "course": "Python"},
    "102": {"name": "Neha", "age": 21, "course": "Data Science"},
    "103": {"name": "Ravi", "age": 19, "course": "Web Development"}
}

# -------- Accessing dictionary --------
print("Student Records:")
for key, value in students.items():
    print(key, ":", value)

# -------- Update an entry --------
students["102"]["age"] = 22   # Updating age
print("\nAfter updating Neha's age:", students["102"])

# -------- Delete an entry --------
del students["103"]
print("\nAfter deleting student 103:")
print(students)

# -------- Convert dictionary to JSON and save to file --------
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nData saved to students.json")

# -------- Read JSON back into Python --------
with open("students.json", "r") as file:
    loaded_data = json.load(file)

# -------- Clean formatted output --------
print("\nStudent Records from JSON file:")
for roll_no, details in loaded_data.items():
    print(f"Roll No: {roll_no}")
    print(f"Name: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"Course: {details['course']}")
    print("----------------------")
