# Employee_Logic.py

class EmployeeLogic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper
        
    def add_new_employee(self, id, name, address, cell_phone, email, title, home_phone="None", current_trip="None", plane_licenses="None"):
        if self.verify_employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses) == True:
            pass
            #self.data_wrapper.add_employee(id, name, address, cell_phone, email, title, home_phone, current_trip, plane_licenses)
        else:
            print("Invalid Data")
    def update_employee(self, id, new_data):
        self.data_wrapper.modify_employee(id, new_data)

    ##### BELOW NEEDS FIXING #####
    def verify_employee(self, id, name, address, cell_phone, email, title, home_phone="None", current_trip="None", plane_licenses="None"):
        possible = True
        if possible ==True:
            if len(id) != 10 and id.isnumeric()==False:
                possible = False
            elif len(name)<3:
                possible = False
            elif len(address)<3:
                possible = False
            elif len(cell_phone)!=7:
                possible = False
            elif len(email)<6:
                possible = False
            elif title != "Pilot" and title != "Cabin Crew":
                possible = False
            elif len(home_phone)!=7 and home_phone != "None":
                possible = False
        if possible == True:
            return True
        else:
            return False

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
