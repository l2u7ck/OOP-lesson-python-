class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, marks):
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.marks:
                lecturer.marks[course] += [marks]
            else:
                lecturer.marks[course] = [marks]
        else:
            return 'Ошибка'

    def __str__(self):
        sumall = 0
        count = 0
        for mark in self.grades.values():
            sumall += sum(mark)
            count += len(mark)
        srmarks = sumall / count
        return (f"Имя: {self.name}"
                f"\nФамилия: {self.surname}"
                f"\nСредняя оценка за домашнее задание: {srmarks}"
                f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"
                f"\nЗавершенные курсы: {', '.join(self.finished_courses)}")



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.marks = {}

    def __str__(self):
        sumall = 0
        count = 0
        for mark in self.marks.values():
            sumall += sum(mark)
            count += len(mark)
        srmarks = sumall / count
        return (f"Имя: {self.name}"
                f"\nФамилия: {self.surname}"
                f"\nСредняя оценка за лекции: {srmarks}")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 6)

cool_lecturer = Lecturer('Fred', 'Black')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Fred', 'Black')
cool_lecturer2.courses_attached += ['Git']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer2, 'Git', 9)

print(cool_lecturer.marks)
print(cool_lecturer2.marks)
print(best_student)
