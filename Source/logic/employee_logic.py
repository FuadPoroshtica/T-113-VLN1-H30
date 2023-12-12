# employee_logic.py
class Employee_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def add_new_employee(self, employee):
        self.data_wrapper.add_employee(employee)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()

    def get_pilots(self):
        return [x for x in self.data_wrapper.get_all_employees() if x.title == "Pilot"]

    def get_cabin_crew(self):
        return [x for x in self.data_wrapper.get_all_employees() if x.title != "Pilot"]

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
