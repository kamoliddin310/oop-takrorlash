class Student:
    def __init__(self, student_id, name, age):
        self.id          = student_id
        self.talaba_ismi = name
        self.yoshi       = age
        self.courses = []
        self.grades = []

    def enroll(self, course):
        self.courses.append(course)

    def add_grade(self, course, grade):
        self.grades.append((course, grade))

    def get_grade(self, course):
        for c, g in self.grades:
            if c == course:
                return g
        return 

    def get_courses(self):
        return self.courses
    
a = Student(1, "Ali", 20)
a.enroll("Jsmoniy tarbiya")
a.add_grade("matematika", 95)

print(a.get_grade("matematika"))
print(a.get_courses())