#logic_wrapper.py
from logic.employee_logic import Employee_Logic
from logic.location_logic import Location_Logic
from logic.plane_logic import Plane_Logic

class Logic_Wrapper:
    def __init__(self, data_wrapper):
        self.employee_logic = Employee_Logic(data_wrapper)
        self.location_logic = Location_Logic(data_wrapper)
        self.plane_logic = Plane_Logic(data_wrapper)

    # Employee related methods
    def add_employee(self, employee):
        self.employee_logic.add_new_employee(employee)
    
    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

    def get_employee_by_id(self, employee_id):
        return self.employee_logic.get_employee_by_id(employee_id)

    def update_employee(self, employee_id, new_data):
        self.employee_logic.update_employee(employee_id, new_data)

    # Location related methods
    def add_location(self, location):
        self.location_logic.add_new_location(location)

    def get_all_locations(self):
        return self.location_logic.get_all_locations()

    def get_location_by_id(self, location_id):
        return self.location_logic.get_location_by_id(location_id)

    def update_location(self, location_id, new_data):
        self.location_logic.update_location(location_id, new_data)

    # Plane related methods
    def add_plane(self, plane):
        self.plane_logic.add_new_plane(plane)

    def get_all_planes(self):
        return self.plane_logic.get_all_planes()

    def get_plane_by_id(self, plane_id):
        return self.plane_logic.get_plane_by_id(plane_id)

    def update_plane(self, plane_id, new_data):
        self.plane_logic.update_plane(plane_id, new_data)