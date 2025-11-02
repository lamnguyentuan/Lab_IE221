from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__ (self, ID, name, baseSalary, responsibilityIndex):
        self._ID = ID
        self._name = name
        self._baseSalary = baseSalary
        self._responsibilityIndex = responsibilityIndex

    @abstractmethod
    def calculateSalary(self):
        pass

    def displayInfo(self):
        print(f"ID: {self._ID}, Name: {self._name}, Base Salary: {self._baseSalary}, Responsibility Index: {self._responsibilityIndex}, Total Salary: {self.calculateSalary()}")

    def getId(self):
        return self._ID
    
    def getName(self):
        return self._name
    
    def setBaseSalary(self, newBaseSalary):
        self._baseSalary = newBaseSalary

class Specialist(Staff):
    def __init__(self, ID, name, baseSalary, responsibilityIndex, overTimeHours):
        super().__init__(ID, name, baseSalary, responsibilityIndex)
        self.__overTimeHours = overTimeHours

    def calculateSalary(self)->float:
        return self._baseSalary + self._baseSalary * self._responsibilityIndex + self.__overTimeHours * 180000



class Researcher(Staff):
    def __init__(self, ID, name, baseSalary, responsibilityIndex, numOfInnovations):
        super().__init__(ID, name, baseSalary, responsibilityIndex)
        self.__numOfInnovations = numOfInnovations

    def calculateSalary(self)->float:
        return self._baseSalary + self._baseSalary * (self._responsibilityIndex-0.2) + self.__numOfInnovations * 5500000


class Manager(Staff):
    def __init__(self, ID, name, baseSalary, responsibilityIndex, concurrentIndex):
        super().__init__(ID, name, baseSalary, responsibilityIndex)
        self.__concurrentIndex = concurrentIndex

    def calculateSalary(self)->float:
        return self._baseSalary*0.7+ self._baseSalary * self._responsibilityIndex + self.__concurrentIndex * 2000000


if __name__ == "__main__":

    """Khoi tao danh sach nhan vien"""
    listStaff = [
        Specialist("S001", "Alice", 10000000, 0.1, 10),
        Researcher("R001", "Bob", 12000000, 0.3 , 2),
        Manager("M001", "Charlie", 15000000, 0.4, 3),
        Manager("M002", "David", 20000000, 0.5, 5),
        Specialist("S002", "Eve", 11000000, 0.2, 5),
        Manager("M003", "Frank", 18000000, 0.35, 4),
        Researcher("R002", "Grace", 13000000, 0.25 , 1)
    ]

    """Cau 1: Hien thi thong tin nhan vien"""
    print("\n===== Staff Information =====")
    for staff in listStaff:
        staff._totalSalary = staff.calculateSalary()    
        staff.displayInfo()
    
    """Cau 2: Tinh tong luong phai tra cho tung nhan vien"""
    print("\n===== Total Salary of Each Staff =====")
    for staff in listStaff:
        staff._totalSalary = staff.calculateSalary()
        print(f"Total salary of {staff._name} is: {staff._totalSalary}")

    """Cau 3: Tim kiem nhan vien theo ma nhan vien"""
    print("\n===== Search Staff by ID =====")

    search_id = "M002"
    staffName = ""
    found = False
    for staff in listStaff:
        staffName = staff.getName() if staff.getId() == search_id else ""
        if staffName:
            found = True
            break
    
    if found:
        print(f"Staff with ID {search_id} is: {staffName}")
    else:
        print(f"Staff with ID {search_id} not found.")

    """Cau 4: Tinh tong so tien luong phai tra cho tat ca nhan vien trong cong ty"""
    print("\n===== Total Salary to be Paid by the Company =====")

    totalCompanySalary = sum(staff.calculateSalary() for staff in listStaff)
    print(f"Total salary to be paid by the company: {totalCompanySalary}")

    """Cau 5: Tim ma nhan vien co tong luong lon nhat"""
    print("\n===== Highest Paid Staff =====")
    listHighestPaidStaff = []
        
    highestPaidStaff = max(listStaff, key=lambda staff: staff.calculateSalary())
    for staff in listStaff:
        if staff.calculateSalary() == highestPaidStaff.calculateSalary():
            listHighestPaidStaff.append(staff)

    print(f"Highest paid staff is {highestPaidStaff.getName()} with total salary: {highestPaidStaff.calculateSalary()}")

    """Cau 6: Cap nhat lai luong co ban theo ma nhan vien"""

    print("\n===== Update Base Salary by Staff ID =====")
    update_id = "R001"
    new_base_salary = 14000000
    print(f"Update id is {update_id} and new base salary is {new_base_salary}")
    for staff in listStaff:
        if staff.getId() == update_id:
            staff.setBaseSalary(new_base_salary)
            print(f"Updated base salary of staff ID {update_id} to {new_base_salary}")
            staff.displayInfo()
            break

    """Cau 7: Khoi tao du lieu theo yeu cau cau de bai"""
    print("\n===== Initialize Data as Required =====")
    newLListStaff = [
        Specialist("123", "Nguyen A", 4500000, 0.5, 50),
        Researcher("124", "Nguyen B", 5600000, 1.2, 10),
        Manager("125", "Nguyen C", 7800000, 1.5, 1.3),
        Researcher("126", "Nguyen D", 8100000, 0.8, 12),
        Manager("127", "Nguyen E", 9500000, 1.0, 1.6),
        Specialist("128", "Nguyen F", 6500000, 0.8, 30)
    ]

    print("Initialized staff data:")
    for staff in newLListStaff:
        staff.displayInfo()