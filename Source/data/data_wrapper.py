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

    #Employee
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

    #Flights
    def get_all_flights(self):
        return self.flight_data.flight_constructor()

    def add_flight(self, id,initial_location,arrival_location,employees,plane,start_home,start_foreign,tickets_home,tickets_foreign):
        flight = Flight(id,initial_location,arrival_location,employees,plane,start_home,start_foreign,tickets_home,tickets_foreign)
        self.flight_data.add_flight_data(flight)

    def get_flight_by_id(self, id):
        return self.flight_data.get_flight_by_id(id)

    def modify_flight(self, updated_flight):
        all_flights = self.flight_data.flight_constructor()
        for i, flight in enumerate(all_flights):
            if flight.id == updated_flight.id:
                all_flights[i] = updated_flight
                break
        self.flight_data.modify_flight_data(all_flights)

    #Location
    def get_all_locations(self):
        return self.location_data.location_constructor()

    def add_location(self,id,country, airport_code, flight_duration, distance, manager_name, emergency_phone):
        location = Location(id,country, airport_code, flight_duration, distance, manager_name, emergency_phone)
        self.location_data.add_location_data(location)

    def get_location_by_id(self, id):
        return self.location_data.get_location_by_id(id)

    def modify_location(self, updated_location):
        all_locations = self.location_data.location_constructor()
        for i, location in enumerate(all_locations):
            if location.id == updated_location.id:
                all_locations[i] = updated_location
                break
        self.location_data.modify_location_data(all_locations)

    #Plane
    def get_all_planes(self):
        return self.plane_data.plane_constructor()

    def add_plane(self,plane_id, airline_name, airplane_model, max_capacity):
        plane = Plane(plane_id, airline_name, airplane_model, max_capacity)
        self.plane_data.add_plane_data(plane)
