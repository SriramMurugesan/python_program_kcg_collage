# Store Student Marks & Find Average
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95
}

total_marks = 0
number_of_students = 0

# Loop through the dictionary
for student in student_marks:
    mark = student_marks[student]
    
    # Add to total
    total_marks = total_marks + mark
    # Count the student
    number_of_students = number_of_students + 1

# Calculate average
average = total_marks / number_of_students

print("Students and Marks:", student_marks)
print("Total sum of marks:", total_marks)
print("Average mark:", average)
