n = int(input())

grades = {}

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in grades:
        grades[student] = []
    grades[student].append(grade)

average_grade = {k: sum(v) / len(v) for k,v in grades.items() if sum(v) / len(v) >= 4.5}
filtred_students = sorted(average_grade.items(), key=lambda x: x[1], reverse=True)
for student, grade in filtred_students:
    print(f'{student} -> {grade:.2f}')