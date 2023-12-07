# Logic_Wrapper.py
from logic.employee_logic import EmployeeLogic

class LogicWrapper:
    def __init__(self, data_wrapper):
        self.employee_logic = EmployeeLogic(data_wrapper)

    def add_employee(self, id, name, address, cell_phone, email, title, home_phone=None, current_trip=None, plane_licenses=None):
        self.employee_logic.add_new_employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses)

    def update_employee(self, id, new_data):
        self.employee_logic.update_employee(id, new_data)
