from abc import ABC, abstractmethod

class Student(ABC):
    def __init__ (self, studentID, name, address, credits, gpa):
        self._studentID = studentID
        self._name = name
        self._address = address
        self._credits = credits
        self._gpa = gpa

    @abstractmethod
    def displayInfo(self):
        pass
    def graduationEligibility(self)->bool:
        pass
    def getGPA(self)->float:
        return self._gpa
    def getName(self)->str:
        return self._name
    def getStudentID(self)->str:
        return self._studentID
    
    
class SecondDegreeStudent(Student):
    def __init__(self, studentID, name, address, credits, gpa, graduateScore):
            super().__init__(studentID, name, address, credits, gpa)
            self._graduateScore = graduateScore

    def displayInfo(self):
            print(f"Student ID: {self._studentID}")
            print(f"Name: {self._name}")
            print(f"Address: {self._address}")
            print(f"Credits: {self._credits}")
            print(f"GPA: {self._gpa}")
            print(f"Graduate Score: {self._graduateScore}")
    
    def graduationEligibility(self)->bool:
            return self._gpa >= 5.0 and self._graduateScore >= 5.0 and self._credits >= 84


class undergraduateStudent(Student):
    def __init__(self, studentID, name, address, credits, gpa, nameOfThesis, thesisScore):
            super().__init__(studentID, name, address, credits, gpa)
            self._nameOfThesis = nameOfThesis
            self._thesisScore = thesisScore

    def displayInfo(self):
            print(f"Student ID: {self._studentID}")
            print(f"Name: {self._name}")
            print(f"Address: {self._address}")
            print(f"Credits: {self._credits}")
            print(f"GPA: {self._gpa}")
            print(f"Thesis Name: {self._nameOfThesis}")
            print(f"Thesis Score: {self._thesisScore}")
    def graduationEligibility(self)->bool:
            return self._gpa >= 5.0 and self._thesisScore >= 5.0 and self._credits >= 120

if __name__ == "__main__":
    """Cau 1: Tao danh sach sinh vien"""
    listStudent = [
    SecondDegreeStudent("23080", "Nguyen Van A", "Ha Noi", 120, 7.5, 8.0),
    undergraduateStudent("23520810", "Ha Van B", "Hai Phong", 130, 8.8, "AI in Education", 9.0),
    undergraduateStudent("23520811", "Le Thi C", "Da Nang", 140, 5.2, "Machine Learning", 7.5),
    SecondDegreeStudent("23081", "Tran Van D", "Ho Chi Minh City", 125, 3.9, 9.5),
    SecondDegreeStudent("23082", "Pham Thi E", "Can Tho", 115, 7.8, 6.5),
    undergraduateStudent("23520812", "Vu Van F", "Nha Trang", 110, 2.5, "Deep Learning", 5.0),
    undergraduateStudent("23520813", "Do Thi G", "Hue", 150, 9.6, "Data Science", 8.5),
    undergraduateStudent("23520814", "Hoang Van H", "Dong Thap", 135, 3.0, "Web Development", 7.0)
    ]

    """Cau 2: Hien thi thong tin tat ca sinh vien"""
    print("Thong tin tat ca sinh vien:")
    print("-----------------------")
    for student in listStudent:
        student.displayInfo()
        print("-----------------------")

    """Cau 3: Liet ke sinh vien du dieu kien tot nghiep"""
    print("Danh sach sinh vien du dieu kien tot nghiep:")  
    print("-----------------------")
    for student in listStudent:
        if student.graduationEligibility():
            print(f"Student ID: {student.getStudentID()}, Name: {student.getName()}")
            print("-----------------------")

    """Cau 4: Liet ke sinh vien khong du dieu kien tot nghiep"""
    print("Danh sach sinh vien khong du dieu kien tot nghiep:")
    print("-----------------------")
    for student in listStudent:
        if not student.graduationEligibility():
            print(f"Student ID: {student.getStudentID()}, Name: {student.getName()}")
            print("-----------------------")
    """Cau 5: Tim sinh vien undergraduate co GPA cao nhat"""
    top_undergraduate = None
    undergraduateStudents = list(filter(lambda s: isinstance(s, undergraduateStudent), listStudent))
    highest_gpa = max(undergraduateStudents, key=lambda s: s.getGPA()).getGPA()
    top_undergraduate_students = list(filter(lambda s: s.getGPA() == highest_gpa, undergraduateStudents))
    print("Sinh vien undergraduate co GPA cao nhat:")
    for student in top_undergraduate_students:
        print(f"Student ID: {student.getStudentID()} - Student Name: {student.getName()} with GPA: {student.getGPA()}")
    print("-----------------------")
    """Cau 6: Xet tot nghiep """
    print("Ket qua xet tot nghiep:")
    for student in listStudent:
        if student.graduationEligibility():
            print(f"Student ID: {student.getStudentID()} - {student.getName()} is eligible for graduation.")
        else:
            print(f"Student ID: {student.getStudentID()} - {student.getName()} is NOT eligible for graduation.")
        print("-----------------------")
    """Cau 7: Tim sinh vien chua du dieu kien tot nghiep"""
    not_eligible_students = list(filter(lambda student: not student.graduationEligibility(), listStudent))
    print("Sinh vien chua du dieu kien tot nghiep:")
    for student in not_eligible_students:
        print(f"Student ID: {student.getStudentID()} - Student Name: {student.getName()}")
        print("-----------------------")
    print("-----------------------")
    """Cau 8: Tim sinh vien du dieu kien tot nghiep"""
    eligible_students = list(filter(lambda student: student.graduationEligibility(), listStudent))
    print("Sinh vien du dieu kien tot nghiep:")
    for student in eligible_students:
        print(f"Student ID: {student.getStudentID()} - Student Name: {student.getName()}")
        print("-----------------------")
    print("-----------------------")


