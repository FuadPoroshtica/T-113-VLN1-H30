import csv
from model.employee_model import Employee

class Employee_data:
    def __init__(self) -> None:
        self.model = "files/employees.csv"

    def employee_constructor(self):
        employee_list = []
        file = csv.DictReader(open(self.model, 'r'))
        for row in file:
            employee_list.append(Employee(row["id"],row["name"],row["address"],row["cell_phone"],row["email"],row["title"],row["home_phone"],row["current_trip"],row["plane_licenses"]))
        return employee_list
    def add_employee_data(self,employee):
        #Employee(id,name,address,cell_phone,email,title,home_phone,current_trip,plane_licenses)
        file = csv.DictReader(open(self.model, 'w'))
    def modify_employee_data(self,id):
        file = csv.DictReader(open(self.model, 'r'))
        for row in file:
            if row["id"]==id:

