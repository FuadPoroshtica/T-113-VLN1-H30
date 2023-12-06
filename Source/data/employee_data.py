import csv
from model.employee_model import Employee

class Employee_data:
    def __init__(self) -> None:
        self.model = "files/employees.csv"
        self.fieldname = ["id","name","address","cell_phone","email","title","home_phone","current_trip","plane_licenses"]
    def employee_constructor(self):
        employee_list = []
        with open(self.model, newline='', encoding="utf-8") as file:
            dict_file = csv.DictReader(file)
            for row in dict_file:
                employee_list.append(Employee(row["id"],row["name"],row["address"],row["cell_phone"],row["email"],row["title"],row["home_phone"],row["current_trip"],row["plane_licenses"]))
        return employee_list
    def add_employee_data(self, employee):
        with open(self.model, 'a', newline='', encoding="utf-8") as file:
            dict_write=csv.DictWriter(file,fieldname=self.fieldname)
            dict_write.writerow({"id":employee.id,"name":employee.name,"address":employee.address,"cell_phone":employee.cell_phone,"email":employee.email,"title":employee.title,"home_phone":employee.home_phone,"current_trip":employee.current_trip,"plane_licenses":employee.plane_licenses})

    def modify_employee_data(self,employee_list,changed_employee):
        with open(self.model,'w', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file,fieldnames=self.fieldname)
            dict_write.writerow({self.fieldname[i]: self.fieldname[i] for i in range(len(self.fieldname))})
            for employee in employee_list:
                print(employee.id,changed_employee.id)
                if employee.id != changed_employee.id:
                    dict_write.writerow({"id":employee.id,"name":employee.name,"address":employee.address,"cell_phone":employee.cell_phone,"email":employee.email,"title":employee.title,"home_phone":employee.home_phone,"current_trip":employee.current_trip,"plane_licenses":employee.plane_licenses})
                else:
                    dict_write.writerow({"id":changed_employee.id,"name":changed_employee.name,"address":changed_employee.address,"cell_phone":changed_employee.cell_phone,"email":changed_employee.email,"title":changed_employee.title,"home_phone":changed_employee.home_phone,"current_trip":changed_employee.current_trip,"plane_licenses":changed_employee.plane_licenses})
