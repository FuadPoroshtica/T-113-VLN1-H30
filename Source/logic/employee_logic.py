from data.employee_data import Employee_data
from model.employee_model import Employee

class EmployeeLogic:
    def __init__(self):
        self.employee_data = Employee_data()

    def getEmployees(self):
        return self.employee_data.employee_constructor()

    def getPilots(self):
        return [emp for emp in self.getEmployees() if emp.title == 'Pilot']

    def getStewards(self):
        return [emp for emp in self.getEmployees() if emp.title == 'Steward']

    def doesEmployeeExist(self, employee_id):
        return any(emp.id == employee_id for emp in self.getEmployees())

    def changeSpecificEmployee(self, employee_id, updated_info):
        # Logic to update employee details
        # You need to define how updated_info is structured and how it updates the employee
        pass

    def searchLicense(self, license_type):
        return [emp for emp in self.getEmployees() if license_type in emp.plane_licenses]

    def licenseSort(self):
        return sorted(self.getEmployees(), key=lambda emp: emp.plane_licenses)
