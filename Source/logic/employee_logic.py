# employee_logic.py
from model.employee_model import Employee 
import datetime
class Employee_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper
        
    def add_new_employee(self, id, name, address, cell_phone, email, title, home_phone="None", current_trip="None", plane_licenses="None"):
        if self.verify_employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses) == True:
            pass
            # add employee currently disabled while testing verify
            # self.data_wrapper.add_employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses)
            
        else:
            print("Invalid Data")
    def update_employee(self, id, new_data):
        self.data_wrapper.modify_employee(id, new_data)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()
    ##### BELOW NEEDS FIXING #####
    def verify_employee(self, id, name, address, cell_phone, email, title, home_phone="None", current_trip="None", plane_licenses="None"):
        possible = True
        if possible ==True:
            if len(id) == 10 and id.isnumeric()==True:
                try:
                    id_year=int(id[4,6])
                    id_month=int(id[2,4])
                    id_day=int(id[0,2])
                    datetime.date(id_year,id_month,id_day)
                except ValueError:
                    possible=False
            elif len(name)<3:
                print(f"name: {name}")
                possible = False
            elif len(address)<3:
                print(f"address: {address}")
                possible = False
            elif len(cell_phone)!=7:
                print(f"cell_phone: {cell_phone}")
                possible = False
            elif len(email)<6:
                print(f"email: {email}")
                possible = False
            elif title.lower() != "pilot" and title.lower() != "cabin crew":
                print(f"title: {title}")
                possible = False
            elif len(home_phone)!=7 and home_phone != "None":
                print(f"home_phone: {home_phone}")
                possible = False
        return possible

    def get_employee_by_id(self, employee_id):
        return self.data_wrapper.get_employee_by_id(employee_id)

    def update_employee_details(self, employee_id, new_details):
        employee = self.get_employee_by_id(employee_id)
        if not employee:
            return

        for key, value in new_details.items():
            if value is not None: 
                setattr(employee, key, value)

        self.data_wrapper.modify_employee(employee)

    def is_employee_a_pilot(self, employee):
        return employee.title.lower() == 'pilot'