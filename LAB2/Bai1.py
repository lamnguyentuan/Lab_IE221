class Staff():
    def __init__ (self, staffID, name, salary, saleProducts, monthlySalary = 0):
        self.__staffID = staffID
        self.__name = name
        self.__salary = salary
        self.__saleProducts = saleProducts

    def calculateSalary(self):
        self.__monthlySalary = self.__salary + (self.__saleProducts * 1750000)
        if self.__salary >= 10000000:
            self.__monthlySalary += self.__monthlySalary * 0.1
        return self.__monthlySalary
    
    def __str__(self) -> str:
        return f"Staff ID: {self.__staffID}\tName: {self.__name}\tSalary: {self.__salary}\tSale Products: {self.__saleProducts}"

    def printInfo(self):
        print(f"Staff ID: {self.__staffID}\tName: {self.__name}\tSalary: {self.__salary}\tSale Products: {self.__saleProducts}")
    
    def getMonthlySalary(self):
        return self.__monthlySalary
    
    def getName(self):
        return self.__name
    
    def getStaffID(self):
        return self.__staffID
    
    def setSalary(self, newSalary):
        self.__salary = newSalary

    def getSaleProducts(self):
        return self.__saleProducts

if __name__ == "__main__":
    """ Cau 1: List of staff initialization """
    listStaff = [
        Staff(1, "Nguyen Van A", 12000000, 3),
        Staff(2, "Tran Thi B", 8000000, 5),
        Staff(3, "Le Van C", 15000000, 2),
        Staff(4, "Pham Thi D", 9000000, 4),
        Staff(5, "Hoang Van E", 11000000, 1),
        Staff(6, "Vu Thi F", 7000000, 6),
        Staff(7, "Dang Van G", 13000000, 0),
        Staff(8, "Bui Thi H", 9500000, 3),
        Staff(9, "Do Van I", 10500000, 2),
        Staff(10, "Phan Thi K", 8500000, 4),
        Staff(11, "Trinh Van L", 11500000, 1),
        Staff(12, "Cao Thi M", 7500000, 5)
    ]

    """Cau 2: Print staff information and calculate monthly salary"""
    for staff in listStaff:
        staff.calculateSalary()
        print(staff)

    """Cau 3: Calculate monthly salary for all staff"""
    for staff in listStaff:
        staff.calculateSalary()
        print(f"Monthly Salary of {staff.getName()}: {staff.getMonthlySalary()}")

    """Cau 4: Find the staff follow by id"""
    searchID = 3
    staffFound = [staff for staff in listStaff if staff.getStaffID() == searchID]
    print(f"Information of staff with ID {searchID}:")
    for staff in staffFound:
        staff.printInfo()

    """Cau 5: Update salary of staff follow by id
           Dùng lại ID = 3 ở câu trên"""
    newSalary = 13000000
    for staff in staffFound:
        staff.setSalary(newSalary)
        staff.calculateSalary()
        print(f"Updated Information of staff with ID {searchID}:")
        staff.printInfo()

    """Cau 6: Find the highest monthly salary"""
    highestSalary = max(listStaff, key=lambda staff: staff.getMonthlySalary())
    print(f"Highest Monthly Salary:")
    highestSalary.printInfo()

    """Cau 7: Find the lowest product sale"""
    lowestSale = min(listStaff, key=lambda staff: staff.getSaleProducts())
    print(f"Lowest Product Sale:")
    lowestSale.printInfo()

    """Cau 8: Find the top 10 staff with highest monthly salary"""
    top10Staff = sorted(listStaff, key=lambda staff: staff.getMonthlySalary(), reverse=True)[:10]
    print(f"Top 10 Staff with Highest Monthly Salary:")
    for staff in top10Staff:
        print(f"Staff ID: {staff.getStaffID()}, Staff Name: {staff.getName()}, Monthly Salary: {staff.getMonthlySalary()}")
    
    """Cau 9: Sort the staff by monthly salary ascending"""
    sortedStaff = sorted(listStaff, key=lambda staff: staff.getMonthlySalary())
    print(f"Staff sorted by Monthly Salary (Ascending):")
    for staff in sortedStaff:
        print(f"Staff ID: {staff.getStaffID()}, Staff Name: {staff.getName()}, Monthly Salary: {staff.getMonthlySalary()}")
    """Cau 10: Sort the staff by name alphabetically"""
    sortedByNameStaff = sorted(listStaff, key=lambda staff: staff.getName())
    print(f"Staff sorted by Name (Alphabetically):")
    for staff in sortedByNameStaff:
        print(f"Staff ID: {staff.getStaffID()}, Staff Name: {staff.getName()}, Monthly Salary: {staff.getMonthlySalary()}")