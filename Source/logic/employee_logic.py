# employee_logic.py
from model.employee_model import Employee 

class EmployeeLogic:
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
            if len(id) != 10 and id.isnumeric()==False:
                possible = False
            elif len(name)<3:
                possible = False
            elif len(address)<3:
                possible = False
            elif len(cell_phone)!=7:
                possible = False
            elif len(email)<6:
                possible = False
            elif title != "Pilot" and title != "Cabin Crew":
                possible = False
            elif len(home_phone)!=7 and home_phone != "None":
                possible = False
        if possible == True:
            return True
        else:
            return False

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