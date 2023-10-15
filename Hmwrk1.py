class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    list_students = []
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lectorier, course, grade):
        if isinstance(lectorier, Lectorier) and course in self.courses_in_progress and course in lectorier.courses_attached:
            if course in lectorier.grades:
                lectorier.grades[course] += [grade]
            else:
                lectorier.grades[course] = [grade]

    def __midgrades(self):
        for course in self.courses_in_progress:
            return sum(self.grades[course]) / len(self.grades[course])

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.__midgrades()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        return self.__midgrades() < other.__midgrades()

    def __gt__(self, other):
        return self.__midgrades() > other.__midgrades()

    def average_grade(self, students, course):
        for student in students:
            return sum(self.grades[course]) / len(self.grades[course])

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lectorier(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    list_lectorirs = []

    def __midgrades(self):
        for course in self.courses_attached:
            return sum(self.grades[course])/len(self.grades[course])

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.__midgrades()}")

    def __lt__(self, other):
        return self.__midgrades() < other.__midgrades()

    def __gt__(self, other):
        return self.__midgrades() > other.__midgrades()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


student_dima = Student('Dima', 'Dimov', 'm')
student_vika = Student('Vika', 'Vikova', 'w')

lectorier_artem = Lectorier('Artem', 'Artemov')
lectorier_karina = Lectorier('Karina', 'Karinova')

reviuwer_pasha = Reviewer('Pasha','Pashov')
reviuwer_masha = Reviewer('Masha', 'Mashina')

student_dima.courses_in_progress += ['Python']
student_dima.courses_in_progress += ['JS']

student_vika.courses_in_progress += ['Python']
student_vika.courses_in_progress += ['Git']

student_dima.add_courses('Git')
student_vika.add_courses('js')

lectorier_karina.courses_attached += ['Python']
lectorier_artem.courses_attached += ['Python']
reviuwer_pasha.courses_attached += ['Python']
reviuwer_masha.courses_attached += ['Python']

student_dima.rate_lector(lectorier_artem, 'Python', 10)
student_dima.rate_lector(lectorier_karina, 'Python', 7)
student_vika.rate_lector(lectorier_artem, 'Python', 9)
student_vika.rate_lector(lectorier_karina, 'Python', 10)

reviuwer_pasha.rate_hw(student_dima, 'Python', 10)
reviuwer_pasha.rate_hw(student_vika, 'Python', 6)
reviuwer_masha.rate_hw(student_dima, 'Python', 9)
reviuwer_masha.rate_hw(student_vika, 'Python', 9)

print(student_vika)
print(student_dima)
print(lectorier_artem)
print(lectorier_karina)
print(reviuwer_pasha)
print(reviuwer_masha)

print(student_dima < student_vika)
print(student_dima > student_vika)
print(lectorier_artem < lectorier_karina)
print(lectorier_artem > lectorier_karina)

list_students = [student_dima, student_vika]
list_lectoriers = [lectorier_artem, lectorier_karina]


def average_grade_students(students, course):
    list_grades = []
    for student in students:
        list_grades.append(sum(student.grades[course]) / len(student.grades[course]))
    return sum(list_grades) / len(list_grades)

print(average_grade_students(list_students, 'Python'))

def average_grade_lectoriers(lectoriers, course):
    list_grades = []
    for lectorier in lectoriers:
        list_grades.append(sum(lectorier.grades[course]) / len(lectorier.grades[course]))
    return sum(list_grades) / len(list_grades)

print(average_grade_lectoriers(list_lectoriers, 'Python'))