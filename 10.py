class Animal:
    def __init__(self, ism: str, yosh: int)-> None:
        self.ism = ism
        self.yosh = yosh
    
    def get_info(self):
        return f"ismi--> {self.ism}, yoshi --> {self.yosh}"

a = Animal("Azee", 12)    
b = Animal("Azee", 14)

print(a.get_info())
print(b.get_info())