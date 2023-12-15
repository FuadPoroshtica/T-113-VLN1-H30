import datetime
# employee_logic.py
class Employee_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def verify_allowed(self, employee, reason):
        employee.name=employee.name.title()
        employee.title=employee.title.title() # note employee.title is job while title() capatilzes the first letter of every word
        employee.address=employee.address.title()
        if type(employee.plane_licenses) == type([]):
            temp_licenses=[]
            for x in employee.plane_licenses:
                x.title()

        errors = []
        if reason == "add":

            if len(employee.id) != 10:
                errors.append("ID needs to be 10 in length.")

            elif employee.id.isnumeric() == False:
                errors.append("ID needs to have only numbers")

            elif any(employee.id == x.id for x in self.get_all_employees()):
                errors.append(f"Employee ID is already in use by {self.get_employee_by_id(employee.id).name}")

            elif len(employee.id) == 10:

                try:
                    year=int(employee.id[4:6])
                    month=int(employee.id[2:4])
                    day=int(employee.id[0:2])
                    employee_date=datetime.date(year,month,day) # uses date class from datetime package to check for accurate dates
                    current_year=datetime.datetime.now().year
                    if employee.title == "Pilot":

                        if employee_date.year - current_year > 65:
                            errors.append("You aren't premitted to be a Pilot over 65")

                        if employee_date.year - current_year < 21:
                            errors.append("You need to be atleast 21 to become a Commercial Pilot")

                    elif employee_date.year - current_year < 18:
                        errors.append("You need to be 18+ to be a Cabin Crew Member")

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

        if employee.cell_phone.isnumeric() != True or len(employee.cell_phone) != 7:
            errors.append("Your phone number needs to be 7 numbers long")
        if employee.home_phone.isnumeric() != True or len(employee.home_phone) != 7:
            employee.home_phone="None"

        if employee.title != "Cabin Crew" and employee.title != "Pilot":
            errors.append("Job title currently only supports Pilot or Cabin Crew")
        #can't verify yet current_trip
        #can't verify plane_licenses as we don't have a database of different plane licenses.

        if len(employee.address) >20:
            errors.append("Home Address is too long please no more than 20 characters")

        elif len(employee.address) <5:
            errors.append("Home Address needs to be atleast 5 characters")

        if len(errors) != 0:
            return errors
        
    def add_new_employee(self, employee):
        condition = self.verify_allowed(employee,"add")
        if type(condition) == type([]):
            return condition
        else:
            if employee.plane_licenses != "None":
                str_licenses = ":".join(employee.plane_licenses)
                employee.plane_licenses = str_licenses
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

        condition = self.verify_allowed(employee,"modify")
        if type(condition) == type([]):
            return condition
        else:
            #if employee:
            for key, value in new_data.items():
                if value is not None:
                    if key == "plane_licenses":
                        str_licenses = ":".join(value)
                        setattr(employee, key, str_licenses)
                    else:
                        setattr(employee, key, value)
            self.data_wrapper.modify_employee(employee)
            return "Succesfully added employee"



    def is_employee_a_pilot(self, employee_id):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            return employee.title.lower() == "pilot"
        return False
    
