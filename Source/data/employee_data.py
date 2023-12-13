#employee_data.py
import csv
from model.employee_model import Employee

class Employee_Data:
    def __init__(self) -> None:
        self.model = "files/employees.csv"
        self.fieldname = [
            "id", 
            "name", 
            "address", 
            "cell_phone", 
            "email", 
            "title", 
            "home_phone", 
            "current_trip", 
            "plane_licenses"]

    def employee_constructor(self):
        employee_list = []
        with open(self.model, newline='', encoding="utf-8") as file:
            dict_file = csv.DictReader(file)
            for row in dict_file:
                employee_list.append(Employee(
                    row["id"], 
                    row["name"], 
                    row["address"], 
                    row["cell_phone"], 
                    row["email"], 
                    row["title"], 
                    row["home_phone"], 
                    row["current_trip"], 
                    row["plane_licenses"]))
        return employee_list

    def add_employee_data(self, employee):
        with open(self.model, 'a', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file, fieldnames=self.fieldname)  
            if file.tell() == 0:  
                dict_write.writeheader()
            dict_write.writerow({
                "id": employee.id, 
                "name": employee.name, 
                "address": employee.address, 
                "cell_phone": employee.cell_phone, 
                "email": employee.email, 
                "title": employee.title, 
                "home_phone": employee.home_phone, 
                "current_trip": employee.current_trip, 
                "plane_licenses": employee.plane_licenses})

    def get_employee_by_id(self, id):
        all_employees = self.employee_constructor()
        for employee in all_employees:
            if employee.id == id:
                return employee
        return None
    
    def modify_employee_data(self, updated_employee_list):
        with open(self.model, 'w', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file, fieldnames=self.fieldname)
            dict_write.writeheader()
            for employee in updated_employee_list:
                dict_write.writerow({
                    "id": employee.id, 
                    "name": employee.name, 
                    "address": employee.address, 
                    "cell_phone": employee.cell_phone, 
                    "email": employee.email, 
                    "title": employee.title, 
                    "home_phone": employee.home_phone, 
                    "current_trip": employee.current_trip, 
                    "plane_licenses": employee.plane_licenses
                })
    
    def get_all_employee_licenses(self):
        license_dict = {}
        all_employees = self.employee_constructor()
        for employee in all_employees:
            if employee.plane_licenses in [None, "None", ""]:
                continue  

            licenses_str = employee.plane_licenses.replace('[', '').replace(']', '').replace("'", "")
            licenses = [license.strip() for license in licenses_str.split(';') if license]
            for license in licenses:
                if ',' in license:  
                    sub_licenses = [sub_license.strip() for sub_license in license.split(',')]
                    for sub_license in sub_licenses:
                        license_dict.setdefault(sub_license, []).append((employee.id, employee.name))
                else:
                    license_dict.setdefault(license, []).append((employee.id, employee.name))
        return license_dict

