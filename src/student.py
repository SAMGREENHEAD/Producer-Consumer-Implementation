class ITstudent:
    def __init__(self, name, student_id, program, courses):
        self.name = name
        self.student_id = student_id
        self.program = program
        self.courses = courses

    def calculate_average(self):
        # Method to calculate the average mark of the student
        if len(self.courses) > 0:  # Check if the student has taken any courses
            total_mark = sum(course['mark'] for course in self.courses)  # Calculate the total marks
            return total_mark / len(self.courses)  # Return the average mark
        else:
            return 0  # If no courses, return 0 as the average

    def passed(self):
        # Method to check if the student has passed based on the average mark
        average = self.calculate_average()  # Get the student's average mark
        return average >= 50  # Return True if average is greater than or equal to 50, otherwise False
