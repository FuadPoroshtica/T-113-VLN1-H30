# logic_wrapper.py
from logic.employee_logic import EmployeeLogic

class LogicWrapper:
    def __init__(self, data_wrapper):
        self.employee_logic = EmployeeLogic(data_wrapper)

    def add_employee(self, id, name, address, cell_phone, email, title, home_phone=None, current_trip=None, plane_licenses=None):
        self.employee_logic.add_new_employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses)

    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

    def get_employee_by_id(self, employee_id):
        return self.employee_logic.get_employee_by_id(employee_id)

    def is_employee_a_pilot(self, employee_id):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            return self.employee_logic.is_employee_a_pilot(employee)
        return False

    def update_employee_details(self, employee_id, new_details):
        self.employee_logic.update_employee_details(employee_id, new_details)

    def update_employee(self, id, new_data):
        self.employee_logic.update_employee(id, new_data)
