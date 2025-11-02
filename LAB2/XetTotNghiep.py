from typing import List, Dict, Optional
from datetime import datetime

class Program:
    def __init__(self, programID, programName):
        self.__programID = programID
        self.__programName = programName
        self.__creditsRequired = 113
        self.__EnglishCreditsRequired = 12
        self.__miniumGPA = 5.0
        self.__EnglishCertificateRequired = True

    def displayProgramInfo(self):
        print(f"ID Chương trình: {self.__programID}\nTên Chương trình: {self.__programName}\nTín chỉ yêu cầu: {self.__creditsRequired}\nTín chỉ Tiếng Anh yêu cầu: {self.__EnglishCreditsRequired}")
    
    def getCreditsRequired(self):
        return self.__creditsRequired + self.__EnglishCreditsRequired
    

class Student:
    def __init__(self, studentID, name, age, program):
        self.__studentID = studentID
        self.__name = name
        self.__age = age
        self.__program = program
        self.__completedCredits = 0
        self.__gpa = 0.0
        self.__isEnglishCertificate = False
        self.__EnglishCreditsCompleted = 0
        self.__TypeOfCertificate = ""
        self.__listOfCourses = []
        self.__failedCourses = []

    def addCourse(self, courseName : str, credits : int, grade : float):
        self.__listOfCourses.append({
            "courseName": courseName,
            "credits": credits,
            "grade": grade
        })

       
        if grade < 5.0:
            if courseName not in self.__failedCourses:
                self.__failedCourses.append(courseName)
        else:
       
            if courseName in self.__failedCourses:
                self.__failedCourses.remove(courseName)
        
       
        if "English" in courseName:
            if grade >= 5.0: 
                self.__EnglishCreditsCompleted += credits
        else:
            if grade >= 5.0:
                self.__completedCredits += credits
    
    def updateGPA(self, GPA: Optional[float] = None):
        if GPA is not None:
            self.__gpa = GPA
        else:
            totalPoints = 0.0
            totalCredits = 0
            for course in self.__listOfCourses:
                totalPoints += course["grade"] * course["credits"]
                totalCredits += course["credits"]
            self.__gpa = totalPoints / totalCredits if totalCredits > 0 else 0.0
    
    

    def getGPA(self):
        self.updateGPA()
        return self.__gpa
    
    def setEnglishCertificate(self, hasCertificate: bool, typeOfCertificate: str):
        self.__isEnglishCertificate = hasCertificate
        self.__TypeOfCertificate = typeOfCertificate if hasCertificate else ""

    def canGraduate(self):
        self.updateGPA() 
        programCreditsRequired = self.__program.getCreditsRequired()
        if (self.__completedCredits >= programCreditsRequired and
            self.__gpa >= 5.0 and
            len(self.__failedCourses) == 0):
            if self.__isEnglishCertificate and self.__EnglishCreditsCompleted >= 12:
                return True
        return False
    
    def displayGraduationStatus(self):
        self.updateGPA() 
        programCreditsRequired = self.__program.getCreditsRequired()
        if self.canGraduate():
            print(f"Sinh viên {self.__name} (ID: {self.__studentID}) ĐỦ ĐIỀU KIỆN TỐT NGHIỆP.")
            print(f"Tổng tín chỉ hoàn thành: {self.__completedCredits}, Điểm GPA: {self.__gpa:.2f}, Tín chỉ Tiếng Anh: {self.__EnglishCreditsCompleted}, Chứng chỉ Tiếng Anh: {self.__TypeOfCertificate}")
        else:
            print(f"Sinh viên {self.__name} (ID: {self.__studentID}) KHÔNG ĐỦ ĐIỀU KIỆN TỐT NGHIỆP.")
            print(f"Lý do: ", end="")
            if self.__completedCredits < programCreditsRequired:
                print(f"Thiếu tín chỉ ({self.__completedCredits}/{programCreditsRequired}). ", end="")
            if self.__gpa < 5.0:
                print(f"Điểm GPA quá thấp ({self.__gpa:.2f}). ", end="")
            if len(self.__failedCourses) > 0:
                print(f"Có môn rớt: {', '.join(self.__failedCourses)}. ", end="")   
            if not self.__isEnglishCertificate or self.__EnglishCreditsCompleted < 12:
                print(f"Không đủ yêu cầu tiếng Anh. ", end="")

if __name__ == "__main__":
    """ Initialize Program """
    program = Program("7480201", "Information Technology")
    program.displayProgramInfo()

    """ Initialize Students """
    student1 = Student(1, "Nguyen Van A", 22, program)
    student2 = Student(2, "Tran Thi B", 23, program)

    """ Add Courses for Student 1 """
    student1.addCourse("Mathematics", 15, 8.0)
    student1.addCourse("Physics", 10, 6.5)
    student1.addCourse("English 1", 3, 7.0)
    student1.addCourse("English 2", 3, 6.0)
    student1.addCourse("Programming Basics", 20, 9.0)
    student1.addCourse("Data Structures", 15, 4.5)  # Failed course
    student1.setEnglishCertificate(True, "TOEIC")

    """ Add Courses for Student 2 """
    student2.addCourse("Mathematics", 15, 5.0)
    student2.addCourse("Physics", 10, 4.0)  # Failed course
    student2.addCourse("English 1", 3, 6.0)
    student2.addCourse("English 2", 3, 5.5)
    student2.addCourse("Programming Basics", 20, 7.0)
    student2.addCourse("Data Structures", 15, 6.0)
    student2.setEnglishCertificate(False, "")

    """Graduate Status case given"""
    
    """ Create Student 3 - ELIGIBLE TO GRADUATE """
    student3 = Student(3, "Le Van C", 22, program)
    # Add enough credits to graduate (need 113 + 12 English = 125 total)
    student3.addCourse("Mathematics", 15, 8.5)
    student3.addCourse("Physics", 10, 7.0)
    student3.addCourse("Chemistry", 10, 6.5)
    student3.addCourse("English 1", 3, 8.0)
    student3.addCourse("English 2", 3, 7.5)
    student3.addCourse("English 3", 3, 8.0) 
    student3.addCourse("English 4", 3, 7.0)
    student3.addCourse("Programming Basics", 20, 9.0)
    student3.addCourse("Data Structures", 15, 8.5)
    student3.addCourse("Algorithms", 15, 7.5)
    student3.addCourse("Database Systems", 12, 8.0)
    student3.addCourse("Operating Systems", 10, 7.0)
    student3.addCourse("Computer Networks", 8, 8.5)
    student3.addCourse("Software Engineering", 10, 9.0)
    student3.setEnglishCertificate(True, "IELTS 6.5")
    
    """ Create Student 4 - ELIGIBLE TO GRADUATE """
    student4 = Student(4, "Pham Thi D", 21, program)
    student4.addCourse("Mathematics", 15, 9.0)
    student4.addCourse("Physics", 10, 8.5)
    student4.addCourse("Chemistry", 10, 7.5)
    student4.addCourse("English 1", 3, 9.0)
    student4.addCourse("English 2", 3, 8.5)
    student4.addCourse("English 3", 3, 9.0)
    student4.addCourse("English 4", 3, 8.0)
    student4.addCourse("Programming Basics", 20, 10.0)
    student4.addCourse("Data Structures", 15, 9.5)
    student4.addCourse("Algorithms", 15, 8.5)
    student4.addCourse("Database Systems", 12, 9.0)
    student4.addCourse("Operating Systems", 10, 8.0)
    student4.addCourse("Computer Networks", 8, 9.0)
    student4.addCourse("Software Engineering", 10, 9.5)
    student4.setEnglishCertificate(True, "TOEFL 95")

    """ Display Graduation Status """
    print("=" * 80)
    print("KIỂM TRA ĐIỀU KIỆN TỐT NGHIỆP")
    print("=" * 80)
    print("\n--- Sinh viên 1: Không đủ điều kiện (có môn rớt) ---")
    student1.displayGraduationStatus()
    print()
    print("\n--- Sinh viên 2: Không đủ điều kiện (môn rớt + thiếu chứng chỉ) ---")
    student2.displayGraduationStatus()
    print()
    print("\n--- Sinh viên 3: ĐỦ ĐIỀU KIỆN TỐT NGHIỆP ---")
    student3.displayGraduationStatus()
    print()
    print("\n--- Sinh viên 4: ĐỦ ĐIỀU KIỆN TỐT NGHIỆP ---")
    student4.displayGraduationStatus()
    print()
    print("=" * 80)
