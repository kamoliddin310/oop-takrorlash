class Student:
    Students = []
    def __init__(self, age, name, kursi, familiya):
        self.ism = name
        self.familiya = familiya
        self.yoshi = age
        self.kurs = kursi
        self.baho = []

    def avg_info(self, baho):
        return round(sum(baho) / len(baho))
    
    def add_student(self, talaba):
        self.Students.append(talaba)

    def remove_student(self, talaba):
        self.Students.remove(talaba)
    
    def get_info(self):
        return f"ismi {self.ism} Familiyasi {self.familiya} Yoshi {self.yoshi} Kurs {self.kurs}"

a = Student(19, "Kamoliddin", 1, "Jonxurozov")
s = Student(23, "Azee", 3, "Allanazarov")
d = Student(21, "ddsf", 2, "LAdsd")

print("Urtacha bahosi",a.get_info())
print(a.avg_info([98, 89, 97, 87, 96]))

print(s.add_student("Salomat"))
print(s.get_info())

