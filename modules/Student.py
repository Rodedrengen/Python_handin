class Student():

    x = 10

    def __init__(self,name,gender,datasheet, image_url):

        self.datasheet = datasheet
        self.name = name 
        self.gender = gender
        self.image_url = image_url

    def get_avg_grades(self):
        self.total = 0
        self.average = 0 

        self.grades = self.datasheet.get_grades_as_list()

        for grade in grades:
            self.total = self.total + grade

        average = total / len(grades)

        return average

    def __str__(self):
        
        return self.name + ", " + self.gender + ", " + self.image_url + "\n" + str(self.datasheet)


        