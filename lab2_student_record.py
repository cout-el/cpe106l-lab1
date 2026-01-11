student = {
    "id": "2025-001",
    "name": "Juan Dela Cruz",
    "grades": [88, 90, 85]
}

# 1. Add a grade
new_grade = 92
student["grades"].append(new_grade)

# 2. Update student info
student["name"] = "Juan Q. Dela Cruz"

# Recalculate average
average = sum(student["grades"]) / len(student["grades"])

# 3. Display formatted output
print("-" * 30)
print(f"{'STUDENT RECORD':^30}")
print("-" * 30)
print(f"ID Number:  {student['id']}")
print(f"Full Name:  {student['name']}")
print(f"Grades:     {', '.join(map(str, student['grades']))}")
print("-" * 30)
print(f"GPA Average: {average:.2f}")
print("-" * 30)