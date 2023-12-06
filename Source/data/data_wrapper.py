from data.employee_data import Employee_Data
from data.flight_data import Flight_Data
from data.location_data import Location_Data
from data.plane_data import Plane_Data

class Data_Wrapper:
    def __init__(self):
        self.employee_data = Employee_Data()
        self.flight_data =Flight_Data()
        self.location_data = Location_Data()
        self.plane_data = Plane_Data()

    def get_all_employees(self):
        return self.employee_data.employee_constructor()

    def add_employee(self, id, name, address, cell_phone, email, title, home_phone="None", current_trip="None", plane_licenses="None"):
        self.employee_data.add_employee_data(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses)

    def modify_employee(self, id, type):
        self.employee_data.modify_employee_data(id, type)