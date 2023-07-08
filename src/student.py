class ITstudent:
    def __init__(self, name, student_id, program, courses):
        self.name = name
        self.student_id = student_id
        self.program = program
        self.courses = courses

    def calculate_average(self):
        if len(self.courses) > 0:
            total_mark = sum(course['mark'] for course in self.courses)
            return total_mark / len(self.courses)
        else:
            return 0

    def passed(self):
        average = self.calculate_average()
        return average >= 50
