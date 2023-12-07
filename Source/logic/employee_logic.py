from data.employee_data import Employee_data
from model.employee_model import Employee

class employee_logic:
    def __init__(self):
        self.employee_data = Employee_data()

    def get_employees(self):
        return self.employee_data.employee_constructor()

    def get_pilots(self):
        return [emp for emp in self.get_employees() if emp.title == 'Pilot']

    def get_stewards(self):
        return [emp for emp in self.get_employees() if emp.title == 'Steward']

    def does_employee_exist(self, employee_id):
        return any(emp.id == employee_id for emp in self.get_employees())

    def change_specific_employee(self, employee_id, updated_info):
        # Logic to update employee details
        # You need to define how updated_info is structured and how it updates the employee
        pass

    def search_license(self, license_type):
        return [emp for emp in self.get_employees() if license_type in emp.plane_licenses]

    def license_sort(self):
        return sorted(self.get_employees(), key=lambda emp: emp.plane_licenses)
