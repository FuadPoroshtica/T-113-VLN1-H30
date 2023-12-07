from data.employee_data import Employee_data
from data.flight_data import flight_data
from data.location_data import location_data
from data.plane_data import plane_data
from model.employee_model import Employee

class Data_Wrapper:
    def __init__(self):
        self.employee_data = Employee_data()
        self.flight_data =flight_data()
        self.location_data = location_data()
        self.plane_data = plane_data()

    def get_all_employees(self):
        return self.employee_data.employee_constructor()

    def add_employee(self, id, name, address, cell_phone, email, title, home_phone="None", current_trip="None", plane_licenses="None"):
        employee = Employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses)
        self.employee_data.add_employee_data(employee)
        
    def modify_employee(self, id, type):
        self.employee_data.modify_employee_data(id, type)