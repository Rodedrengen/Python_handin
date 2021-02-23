from .Course import Course
class DataSheet:

    def __init__(self, courses = None):

        self.courses = []

        for course in courses:
            new_course = Course(course.name,
                                course.classroom,
                                course.teacher,
                                course.ECTS,
                                course.grade)
            self.courses.append(new_course)


    def get_grades_as_list(self):

        self.grades = []

        for course in courses:
            grades.append(course.grade)

        return grades

    def __str__(self):
        self.returnString = ""

        for course in self.courses:
            self.returnString = self.returnString + str(course) + "\n"

        return self.returnString
