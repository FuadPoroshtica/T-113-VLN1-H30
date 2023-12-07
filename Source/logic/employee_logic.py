# Employee_Logic.py

class EmployeeLogic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def add_new_employee(self, id, name, address, cell_phone, email, title, home_phone="None", current_trip="None", plane_licenses="None"):
        self.data_wrapper.add_employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses)

    def update_employee(self, id, new_data):
        self.data_wrapper.modify_employee(id, new_data)
