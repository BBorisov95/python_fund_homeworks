data = input()

courses = {}

while not data == 'end':

    course, student = data.split(' : ')

    if course not in courses:
        courses[course] = [student]
    else:
        courses[course].append(student)

    data = input()


ordered_courses = {k: v for k,v in sorted(courses.items(), key=lambda x: -len(x[1]))}

for course, students in ordered_courses.items():
    print(f'{course}: {len(ordered_courses[course])}')
    for student in sorted(students):
        print(f'-- {student}')
