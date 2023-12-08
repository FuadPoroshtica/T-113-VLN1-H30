# employee_logic.py
from model.employee_model import Employee 

class EmployeeLogic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def add_new_employee(self, id, name, address, cell_phone, email, title, home_phone="None", current_trip="None", plane_licenses="None"):
        self.data_wrapper.add_employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses)


    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()

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