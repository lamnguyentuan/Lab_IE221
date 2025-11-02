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
    