students = int(input())
lectures = int(input())
addition_points = int(input())

best_student = 0
attendance_count = 0

for student in range(students):
    attendance = int(input())


    student_attendance = round(attendance / lectures * (5 + addition_points))
    if student_attendance > best_student:
        best_student = student_attendance
        attendance_count = attendance

print(f'Max Bonus: {best_student}.')
print(f'The student has attended {attendance_count} lectures.')