
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Adding grades of lectors
    def rate_lecturer(self, lecturer, course, grades):
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'error'

    # Finding the average score
    def __sr_grades(self):
        all_gr = 0
        count = 0
        for mark in self.grades.values():
            all_gr += sum(mark)
            count += len(mark)
        return all_gr / count

    def __str__(self):
        return (f"Имя: {self.name}"
                f"\nФамилия: {self.surname}"
                f"\nСредняя оценка за домашнее задание: {self.__sr_grades()}"
                f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"
                f"\nЗавершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        return self.__sr_grades() < other.__sr_grades()

    def __eq__(self, other):
        return self.__sr_grades() == other.__sr_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Finding the average score
    def __sr_grades(self):
        all_gr = 0
        count = 0
        for grade in self.grades.values():
            all_gr += sum(grade)
            count += len(grade)
        return all_gr / count

    def __str__(self):
        return (f"Имя: {self.name}"
                f"\nФамилия: {self.surname}"
                f"\nСредняя оценка за лекции: {self.__sr_grades()}")

    def __lt__(self, other):
        return self.__sr_grades() < other.__sr_grades()

    def __eq__(self, other):
        return self.__sr_grades() == other.__sr_grades()


class Reviewer(Mentor):

    # Adding grades of students
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'error'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Create two students
student_1 = Student('Ruby', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ron', 'Skill', 'your_gender')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

# Create Two Reviewer
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Kris', 'Buggy')
reviewer_2.courses_attached += ['Git']

# Adding grades to students
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Git', 9)

# Create two lecturer
lecturer_1 = Lecturer('Fred', 'Black')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Mark', 'Edison')
lecturer_2.courses_attached += ['Git']

# Adding marks to lecturer
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_2, 'Git', 7)
student_1.rate_lecturer(lecturer_2, 'Git', 8)
student_1.rate_lecturer(lecturer_2, 'Git', 10)

student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_2, 'Git', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 9)

# Roll call of all
print(student_1, "\n")
print(student_2, "\n")
print(reviewer_1, "\n")
print(reviewer_2, "\n")
print(lecturer_1, "\n")
print(lecturer_2, "\n")

# Comparison of students
print("Student_1 < student_2:", student_1 < student_2)
print("student_1 == student_2:", student_1 == student_2)

# Comparison of lectors
print("lecturer_1 < lecturer_2:", lecturer_1 < lecturer_2)
print("lecturer_1 == lecturer_2:", lecturer_1 == lecturer_2)


# Calculating the average grade for all students in a given course
def cal_students(st, course):
    sum_grades = 0
    count = 0
    for item in st:
        if (isinstance(item, Student) and (course in item.courses_in_progress or course in item.finished_courses)):
            sum_grades += sum(item.grades[course])
            count += len(item.grades[course])
    # Return of course grade point average
    if count == 0:
        return "Нет оценок"
    else:
        return sum_grades / count


# Calculating the average grade for all lectors in a given course
def cal_lectors(lec, course):
    sum_grades = 0
    count = 0
    for item in lec:
        if (isinstance(item, Lecturer) and course in item.courses_attached):
            sum_grades += sum(item.grades[course])
            count += len(item.grades[course])
    # Return of course grade point average
    if count == 0:
        return "Нет оценок"
    else:
        return sum_grades/count


# Creation of lists
students_list = list()
students_list.append(student_1)
students_list.append(student_2)

lectors_list = list()
lectors_list.append(lecturer_1)
lectors_list.append(lecturer_2)

# Checking functions
print("\nСредний балл среди студентов по курсу Python: ", cal_students(students_list, 'Python'))
print("\nСредний балл среди преподователей по курсу Git: ", cal_lectors(lectors_list, 'Git'))
