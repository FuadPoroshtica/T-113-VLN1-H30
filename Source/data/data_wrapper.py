from data.employee_data import Employee_Data
from data.flight_data import Flight_Data
from data.location_data import Location_Data
from data.plane_data import Plane_Data
from model.employee_model import Employee
from model.flight_model import Flight
from model.location_model import Location
from model.plane_model import Plane

class Data_Wrapper:
    def __init__(self):
        self.employee_data = Employee_Data()
        self.flight_data = Flight_Data()
        self.location_data = Location_Data()
        self.plane_data = Plane_Data()

    def get_all_employees(self):
        return self.employee_data.employee_constructor()

    def add_employee(self, id, name, address, cell_phone, email, title, home_phone="None", current_trip="None", plane_licenses="None"):
        employee = Employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses)
        self.employee_data.add_employee_data(employee)

    def get_employee_by_id(self, id):
        return self.employee_data.get_employee_by_id(id)

    def modify_employee(self, updated_employee):
        all_employees = self.employee_data.employee_constructor()
        for i, employee in enumerate(all_employees):
            if employee.id == updated_employee.id:
                all_employees[i] = updated_employee
                break
        self.employee_data.modify_employee_data(all_employees)
