# data_wrapper.py

from data.employee_data import Employee_data
from model.employee_model import Employee

class Data_Wrapper:
    def __init__(self):
        self.employee_data = Employee_data()

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
