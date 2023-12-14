import datetime
# employee_logic.py
class Employee_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def verify_allowed(self, employee):
        errors = []
        if len(employee.id) != 10:
            errors.append("ID needs to be 10 in length.")

        elif employee.id.isnumeric() == False:
            errors.append("ID needs to have only numbers")

        elif len(employee.id) == 10:
            try:
                year=int(employee.id[4:6])
                month=int(employee.id[2:4])
                day=int(employee.id[0:2])
                datetime.date(year,month,day) # uses date class from datetime package to check for accurate dates
            except ValueError:
                errors.append("ID needs to have legitimate day/month/year")

        if len(employee.name) >35:
            errors.append("Name is too long please no more than 35 characters")

        elif len(employee.name) <5:
            errors.append("Name needs to be atleast 5 characters")

        if " " not in employee.email:
            if "@" in employee.email:
                temp_address=employee.email.split("@")
                if len(temp_address) == 2:                    
                    if temp_address[0] == '':
                        errors.append("you need to write text before the @")
                    if "." in temp_address[1]:
                        temp_address_2=temp_address[1].split(".")
                        if len(temp_address_2)==2:
                            if temp_address_2[0] == '':
                                errors.append("you need text between @ and .")
                            if temp_address_2[1] == '':
                                errors.append("you need a domain suffix example(.com, .is)")
                        else:
                            errors.append("you must have 1 dot (.) in an email")
                    else:
                        errors.append("you need to put a domain for example('gmail.com')")
            else:
                errors.append("you must have 1 @ in an email")
        else:
            errors.append("you can't have spaces in emails")

        #id,name,address,cell_phone,email,title,home_phone,current_trip,plane_licenses

        

        if len(errors) != 0:
            return errors

    def add_new_employee(self, employee):
        condition = self.verify_allowed(employee)
        if type(condition) == type([]):
            return condition
        else:
            self.data_wrapper.add_employee(employee)
            return "Succesfully added employee"
    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()

    def get_pilots(self):
        return [employee for employee in self.data_wrapper.get_all_employees() if employee.title.lower() == "pilot"]

    def get_cabin_crew(self):
        return [employee for employee in self.data_wrapper.get_all_employees() if employee.title.lower() != "pilot"]
    
    def get_employee_by_id(self, employee_id):
        return self.data_wrapper.get_employee_by_id(employee_id)

    def update_employee(self, employee_id, new_data):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            for key, value in new_data.items():
                if value is not None:
                    setattr(employee, key, value)
            self.data_wrapper.modify_employee(employee)

    def is_employee_a_pilot(self, employee_id):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            return employee.title.lower() == "pilot"
        return False
