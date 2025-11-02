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
    def getGPA(self):
        return self._gpa
    def getCredits(self):
        return self._credits
    
class SecondDegreeStudent(Student):
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

class undergraduateStudent(Student):
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

if __name__ == "__main__":
    """Cau 1: Tao danh sach sinh vien"""
    listStudent = [
    SecondDegreeStudent("23080", "Nguyen Van A", "Ha Noi", 120, 3.5, "AI Research", 9.0),
    undergraduateStudent("23520810", "Ha Van B", "Hai Phong", 130, 3.8, 9.0),
    undergraduateStudent("23520811", "Le Thi C", "Da Nang", 140, 3.2, 7.5),
    SecondDegreeStudent("23081", "Tran Van D", "Ho Chi Minh City", 125, 3.9, "Data Science", 9.5),
    SecondDegreeStudent("23082", "Pham Thi E", "Can Tho", 115, 2.8, "Web Development", 6.5),
    undergraduateStudent("23520812", "Vu Van F", "Nha Trang", 110, 2.5, 5.0),
    undergraduateStudent("23520813", "Do Thi G", "Hue", 150, 3.6, 8.5),
    undergraduateStudent("23520814", "Hoang Van H", "Dong Thap", 135, 3.0, 7.0)
    ]

    """Cau 2: Hien thi thong tin tat ca sinh vien"""
    print("Thong tin tat ca sinh vien:")
    for student in listStudent:
        student.displayInfo()
        print("-----------------------")

    """Cau 3: Liet ke sinh vien du dieu kien tot nghiep"""
    print("Danh sach sinh vien du dieu kien tot nghiep:")  
    
