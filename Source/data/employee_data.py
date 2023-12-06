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
        file.close()
        return employee_list
    def add_employee_data(self,id,name,address,cell_phone,email,title,home_phone="None",current_trip="None",plane_licenses="None"):
        file_read=csv.DictReader(open(self.model,'r'))
        column_names=list(dict(list(file_read)[0]))
        file = csv.DictWriter(open(self.model, 'a'),column_names,lineterminator="\n")
        file.writerow({"id":id,"name":name,"address":address,"cell_phone":cell_phone,"email":email,"title":title,"home_phone":home_phone,"current_trip":current_trip,"plane_licenses":plane_licenses})
    def modify_employee_data(self,id,type):
        file = csv.DictReader(open(self.model, 'rw'))
        for row in file:
            if row["id"]==id:
                pass
