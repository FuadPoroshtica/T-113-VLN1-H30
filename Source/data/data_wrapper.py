#data_wrapper.py

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

    """Employees"""
    def get_all_employees(self):
        return self.employee_data.employee_constructor()

    def add_employee(self, employee):
        self.employee_data.add_employee_data(employee)

    def get_employee_by_id(self, id):
        return self.employee_data.get_employee_by_id(id)

    def modify_employee(self, updated_employee):
        all_employees = self.get_all_employees()
        for i, employee in enumerate(all_employees):
            if employee.id == updated_employee.id:
                all_employees[i] = updated_employee
                break
        self.employee_data.modify_employee_data(all_employees)

        #self.employee_data.modify_employee_data(updated_employee)

    """Flights"""
    def add_flight(self, flight):
        self.flight_data.add_flight_data(flight)

    def get_all_flights(self):
        return self.flight_data.flight_constructor()

    def get_flight_by_id(self, id):
        return self.flight_data.get_flight_by_id(id)

    def modify_flight(self, updated_flight):
        all_flights = self.get_all_flights()
        for i, flight in enumerate(all_flights):
            if flight.id == updated_flight.id:
                all_flights[i] = updated_flight
                break
        self.flight_data.modify_flight_data(all_flights)
    
    def get_flights_by_date(self, date):
        return self.flight_data.get_flights_by_date(date)

    def get_flights_by_week(self, start_date):
        return self.flight_data.get_flights_by_week(start_date)

    """Locations"""
    def get_all_locations(self):
        return self.location_data.location_constructor()

    def add_location(self, location):
        self.location_data.add_location_data(location)

    def get_location_by_id(self, id):
        return self.location_data.get_location_by_id(id)

    def modify_location(self, updated_location):
        all_locations = self.get_all_locations()
        for i, location in enumerate(all_locations):
            if location.id == updated_location.id:
                all_locations[i] = updated_location
                break
        self.location_data.modify_location_data(all_locations)

    """Planes"""
    def get_all_planes(self):
        return self.plane_data.plane_constructor()

    def add_plane(self, plane):
        self.plane_data.add_plane_data(plane)

    def get_plane_by_id(self, id):
        return self.plane_data.get_plane_by_id(id)

    def modify_plane(self, updated_plane):
        all_planes = self.get_all_planes()
        for i, plane in enumerate(all_planes):
            if plane.id == updated_plane.id:
                all_planes[i] = updated_plane
                break
        self.plane_data.modify_plane_data(all_planes)

    """Employee Flight Schedule """
    def update_flight_crew(self, flight_id, crew_list):
        flight = self.flight_data.get_flight_by_id(flight_id)
        if flight:
            flight.employees = crew_list
            self.flight_data.modify_flight_data(flight)

    def update_employee_schedule(self, employee_id, flight_id):
        employee = self.employee_data.get_employee_by_id(employee_id)
        if employee:
            if employee.current_trip:
                employee.current_trip += f',{flight_id}'
            else:
                employee.current_trip = flight_id
            self.employee_data.modify_employee_data(employee)
