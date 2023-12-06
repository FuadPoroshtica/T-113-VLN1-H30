import csv
from model.employee_model import Employee

class Employee_data:
    def __init__(self) -> None:
        self.model = "files/employees.csv"

    def employee_constructor(self):
        employee_list = []
        with open(self.model, newline='', encoding="utf-8") as file:
            dict_file = csv.DictReader()
            for row in dict_file:
                employee_list.append(Employee(row["id"],row["name"],row["address"],row["cell_phone"],row["email"],row["title"],row["home_phone"],row["current_trip"],row["plane_licenses"]))
        return employee_list
    def add_employee_data(self, employee):
        with open(self.model, 'a', newline='', encoding="utf-8") as file:
            fieldnames = ["id","name","address","cell_phone","email","title","home_phone","current_trip","plane_licenses"]
            dict_write=csv.DictWriter(file,fieldnames=fieldnames)
            dict_write.writerow({"id":employee.id,"name":employee.name,"address":employee.address,"cell_phone":employee.cell_phone,"email":employee.email,"title":employee.title,"home_phone":employee.home_phone,"current_trip":employee.current_trip,"plane_licenses":employee.plane_licenses})
 

    def modify_employee_data(self,id,type):
        file = csv.DictReader(open(self.model, 'rw'))
        for row in file:
            if row["id"]==id:
                pass
