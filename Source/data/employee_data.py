import csv
from model.employee_model import Employee
class Employee_data:
    def __init__(self) -> None:
        self.model = "files/employee.csv"
    def employeeConstructor(self):
        employee_list = []
        file = csv.DictReader(open(self.employee, 'r'))
        for line in file:
            print(line)
    def addEmployeeData(self):
        for line in self.employee:
            pass
    def modifyEmployeeData(self):
        for line in self.employee:
            pass
a = Employee_data
a.employeeConstructor()