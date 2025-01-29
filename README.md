# Studentlarni boshlashirish

## **1. `Student` (Talaba) Klass**  
Talaba haqidagi ma’lumotlarni saqlaydi va boshqaradi.  

### **Atributlar:**  
- `student_id` – Talabaning ID raqami  
- `name` – Talabaning ismi  
- `age` – Talabaning yoshi  
- `courses` – Ro‘yxatdan o‘tgan kurslar (`list`)  
- `grades` – Har bir kurs bo‘yicha baholar (`dict`)  

### **Metodlar:**  
✔ `enroll(course)` – Talabani kursga yozish  
✔ `add_grade(grade)` – Baho qo‘shish  
✔ `get_grades()` – Barcha baholarni chiqarish  
✔ `get_courses()` – Ro‘yxatdan o‘tgan kurslarni chiqarish  

---

## **2. `Course` (Kurs) Klass**  
Universitetdagi kurslar haqidagi ma’lumotlarni saqlaydi.  

### **Atributlar:**  
- `course_name` – Kurs nomi  
- `instructor` – O‘qituvchi ismi  
- `students` – Kursga yozilgan talabalar ro‘yxati (`list`)  

### **Metodlar:**  
✔ `add_student(student)` – Kursga talaba qo‘shish  
✔ `remove_student(student)` – Kursdan talabani olib tashlash  
✔ `get_students()` – Kursga yozilgan barcha talabalarni chiqarish  


## **3. `University` (Universitet) Klass**  
Universitetda mavjud bo‘lgan talabalar va kurslarni boshqaradi.  

### **Atributlar:**  
- `name` – Universitet nomi  
- `students` – Universitetga ro‘yxatdan o‘tgan talabalar (`dict` - ID orqali saqlanadi)  
- `courses` – Universitetdagi mavjud kurslar (`dict` - kurs kodlari orqali saqlanadi)  

### **Metodlar:**  
✔ `add_student(student)` – Universitetga yangi talaba qo‘shish  
✔ `add_course(course)` – Universitetga yangi kurs qo‘shish  
✔ `get_student(student_id)` – ID bo‘yicha talabani topish  
✔ `get_course(course_code)` – Kod bo‘yicha kursni topish  
✔ `list_students()` – Universitetdagi barcha talabalarni chiqarish  
✔ `list_courses()` – Universitetdagi barcha kurslarni chiqarish  

