class Course:

    def __init__(self, name, classroom, teacher, ECTS, grade = None):

        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade

    def __str__(self):
        return "Course name: "+self.name + ", Classroom: " + self.classroom + ", Teacher: " + self.teacher + ", ECTS: " + str(self.ECTS) + ", Grade: " + str(self.grade)