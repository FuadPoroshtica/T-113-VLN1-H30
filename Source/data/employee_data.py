import csv, os
from model.employee_model import Employee

class Employee_data:
    def __init__(self) -> None:
        self.model = "files/employees.csv"

    def employeeConstructor(self):
        employee_list = []
        file = csv.DictReader(open(self.model, 'r'))
        for line in file:
            print(line)

    def addEmployeeData(self):
        pass

    def modifyEmployeeData(self):
        pass