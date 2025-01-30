class Course:
    students = []

    def __init__(self, kurs_nomi, uqituvchi_ismi) ->None:
        self.kurs = kurs_nomi
        self.ustoz_ismi = uqituvchi_ismi

    def add_student(self, talaba):
            self.students.append(talaba)
    
    def remove_student(self, student):
         self.students.remove(student)

    def get_info(self):
         return f"ismi {self.students}"
    
    
s = Course("Matem", "Zafar")
s.add_student("Muzafar")
s.add_student("Ali")
s.add_student("Jafar")

print(s.get_info())

s.remove_student("Ali")
print("qolganlar")
print(s.get_info())