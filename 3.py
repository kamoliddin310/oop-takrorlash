class University:
    def __init__(self, name):
        self.name = name
        self.students = {[]}
        self.courses = {[]}

    def add_student(self, student):
        self.students.add(student)

    def add_courses(self, course):
        self.courses.add(course)
    
    def get_student(self, id_student):
        student = list(filter(lambda s: s.id == id_student, self.students))
        return student[0] if student else None

    def get_course(self, course_code):
        pass

    def list_student(self):
        pass

    def list_courses(self):
        pass
    