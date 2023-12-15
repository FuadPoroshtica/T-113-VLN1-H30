import datetime
from datetime import datetime, timedelta, date

# employee_logic.py
class Employee_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def verify_allowed(self, employee, reason):
        employee.name = employee.name.title()
        employee.title = employee.title.title()  # note employee.title is job while title() capitalizes the first letter of every word
        employee.address = employee.address.title()
        if isinstance(employee.plane_licenses, list):
            for x in employee.plane_licenses:
                x.title()

        errors = []
        if reason == "add":
            if len(employee.id) != 10:
                errors.append("ID needs to be 10 in length.")
            elif not employee.id.isnumeric():
                errors.append("ID needs to have only numbers")
            elif any(employee.id == x.id for x in self.get_all_employees()):
                errors.append(f"Employee ID is already in use by {self.get_employee_by_id(employee.id).name}")

            elif len(employee.id) == 10:
                try:
                    year = int(employee.id[4:6]) + 2000  # Assuming the year is in 21st century
                    month = int(employee.id[2:4])
                    day = int(employee.id[0:2])
                    employee_date = date(year, month, day)  # uses date class from datetime package to check for accurate dates
                    current_year = datetime.now().year
                    age = current_year - employee_date.year
                    if employee.title == "Pilot":
                        if age > 65:
                            errors.append("You aren't permitted to be a Pilot over 65")
                        if age < 21:
                            errors.append("You need to be at least 21 to become a Commercial Pilot")

                    elif age < 18:
                        errors.append("You need to be 18+ to be a Cabin Crew Member")

                except ValueError:
                    errors.append("ID needs to have legitimate day/month/year")

            if len(employee.name) > 35:
                errors.append("Name is too long please no more than 35 characters")
            elif len(employee.name) < 5:
                errors.append("Name needs to be at least 5 characters")

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
    
    def get_employee_licenses(self,plane):
        license_dict = {}
        employees = self.employee_constructor()

        for x in self.get_pilots():
            l = []            
        for employee in all_employees:
            if employee.plane_licenses in [None, "None", ""]:
                continue  
            
            licenses_str = employee.plane_licenses.replace('[', '').replace(']', '').replace("'", "")
            licenses = [license.strip() for license in licenses_str.split(';') if license]
            for license in licenses:
                if ',' in license:  
                    sub_licenses = [sub_license.strip() for sub_license in license.split(',')]
                    for sub_license in sub_licenses:
                        license_dict.setdefault(sub_license, []).append((employee.id, employee.name))
                else:
                    license_dict.setdefault(license, []).append((employee.id, employee.name))
        return license_dict

    def get_available_pilots(self, target_flight):
        all_pilots = self.get_pilots()
        available_pilots = []
        for pilot in all_pilots:
            if self._is_pilot_available(pilot, target_flight) and self._has_pilot_license(pilot, target_flight.plane):
                available_pilots.append(pilot)
        return available_pilots
    
    def add_pilot_to_flight(self, flight_id, pilot_id):
        flight = self.data_wrapper.get_flight_by_id(flight_id)
        if not flight:
            return False

        pilot = self.get_employee_by_id(pilot_id)
        if not pilot or not self._is_pilot_available(pilot, flight) or not self._has_pilot_license(pilot, flight.plane):
            return False

        flight.employees.append(pilot_id)
        self.data_wrapper.modify_flight(flight)
        return True

    def get_available_stewards(self, flight):
        all_stewards = self.get_cabin_crew()
        available_stewards = [steward for steward in all_stewards if self._is_steward_available(steward, flight)]
        return available_stewards

    def add_steward_to_flight(self, flight_id, steward_id):
        flight = self.data_wrapper.get_flight_by_id(flight_id)
        if not flight:
            return False

        steward = self.get_employee_by_id(steward_id)
        if not steward or not self._is_steward_available(steward, flight):
            return False

        flight.employees.append(steward_id)
        self.data_wrapper.modify_flight(flight)
        return True

    def _is_pilot_available(self, pilot, target_flight):
        # Get target flight's start and end time
        target_start = datetime.strptime(target_flight.start_home, "%Y-%m-%d %H:%M")
        target_location = self.location_logic.get_location_by_airport_code(target_flight.arrival_location)
        target_flight_duration = target_location.flight_duration if target_location else 0
        target_total_duration = (2 * target_flight_duration) + 60
        target_end = target_start + timedelta(minutes=target_total_duration)

        all_flights = self.data_wrapper.get_all_flights()
        for flight in all_flights:
            if pilot.id in flight.employees and flight.id != target_flight.id:
                flight_start = datetime.strptime(flight.start_home, "%Y-%m-%d %H:%M")
                flight_location = self.location_logic.get_location_by_airport_code(flight.arrival_location)
                flight_duration = flight_location.flight_duration if flight_location else 0
                flight_total_duration = (2 * flight_duration) + 60
                flight_end = flight_start + timedelta(minutes=flight_total_duration)

                if self._times_overlap(target_start, target_end, flight_start, flight_end):
                    return False
        return True

    def _is_steward_available(self, steward, target_flight):
        target_start = datetime.strptime(target_flight.start_home, "%Y-%m-%d %H:%M")
        target_location = self.location_logic.get_location_by_airport_code(target_flight.arrival_location)
        target_flight_duration = target_location.flight_duration if target_location else 0
        target_total_duration = (2 * target_flight_duration) + 60
        target_end = target_start + timedelta(minutes=target_total_duration)

        all_flights = self.data_wrapper.get_all_flights()
        for flight in all_flights:
            if steward.id in flight.employees and flight.id != target_flight.id:
                flight_start = datetime.strptime(flight.start_home, "%Y-%m-%d %H:%M")
                flight_location = self.location_logic.get_location_by_airport_code(flight.arrival_location)
                flight_duration = flight_location.flight_duration if flight_location else 0
                flight_total_duration = (2 * flight_duration) + 60
                flight_end = flight_start + timedelta(minutes=flight_total_duration)

                if self._times_overlap(target_start, target_end, flight_start, flight_end):
                    return False
        return True

    def _times_overlap(self, start1, end1, start2, end2):
        return max(start1, start2) < min(end1, end2)

    def _get_flight_datetime_range(self, start_home, total_duration):
        start_datetime = datetime.strptime(start_home, "%Y-%m-%d %H:%M")
        end_datetime = start_datetime + timedelta(minutes=total_duration)
        return start_datetime, end_datetime


    def _has_pilot_license(self, pilot, plane_id):
        plane = self.data_wrapper.get_plane_by_id(plane_id)
        if plane and pilot.plane_licenses:
            return plane.airplane_model in pilot.plane_licenses.split(':')
        return False

    def _flights_overlap(self, flight1, flight2):
        start1 = datetime.strptime(flight1.start_home, "%Y-%m-%d %H:%M")
        end1 = datetime.strptime(flight1.start_foreign, "%Y-%m-%d %H:%M")
        start2 = datetime.strptime(flight2.start_home, "%Y-%m-%d %H:%M")
        end2 = datetime.strptime(flight2.start_foreign, "%Y-%m-%d %H:%M")
        return max(start1, start2) < min(end1, end2)
    
