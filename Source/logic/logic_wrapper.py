#logic_wrapper.py
from datetime import datetime
from logic.employee_logic import Employee_Logic
from logic.location_logic import Location_Logic
from logic.plane_logic import Plane_Logic
from data.data_wrapper import Data_Wrapper
from logic.flight_logic import Flight_Logic

class Logic_Wrapper:
    def __init__(self, data_wrapper):
        self.employee_logic = Employee_Logic(data_wrapper)
        self.location_logic = Location_Logic(data_wrapper)
        self.plane_logic = Plane_Logic(data_wrapper)
        self.flight_logic = Flight_Logic(data_wrapper, self.location_logic, self.employee_logic)

        self.data_wrapper = Data_Wrapper()


    """Employee related methods"""
    def add_employee(self, employee):
        return self.employee_logic.add_new_employee(employee)
    
    def get_all_employees(self):
        return self.employee_logic.get_all_employees()
    
    def get_pilots(self):
        return self.employee_logic.get_pilots()
    
    def get_cabin_crew(self):
        return self.employee_logic.get_cabin_crew()
    
    def get_employee_by_id(self, employee_id):
        return self.employee_logic.get_employee_by_id(employee_id)

    def update_employee(self, employee_id, new_data):
        self.employee_logic.update_employee(employee_id, new_data)
    
    def is_employee_a_pilot(self, employee_id):
        return self.employee_logic.is_employee_a_pilot(employee_id)
    
    def get_all_plane_licenses(self):
        licenses = self.data_wrapper.get_all_employee_licenses()
        return licenses if licenses is not None else {}
    
    def get_pilots_by_plane_type(self, plane_type):
        all_pilots = self.get_pilots()
        licensed_pilots = [pilot for pilot in all_pilots if plane_type in pilot.plane_licenses]
        return licensed_pilots

    """Location related methods """
    def add_location(self, location):
        self.location_logic.add_new_location(location)

    def get_all_locations(self):
        return self.location_logic.get_all_locations()

    def get_location_by_id(self, location_id):
        return self.location_logic.get_location_by_id(location_id)

    def update_location(self, location_id, new_data):
        return self.location_logic.update_location(location_id, new_data)

    """Plane related methods"""
    def add_plane(self, plane):
        self.plane_logic.add_new_plane(plane)

    def get_all_planes(self):
        return self.plane_logic.get_all_planes()

    def get_plane_by_id(self, plane_id):
        return self.plane_logic.get_plane_by_id(plane_id)

    def update_plane(self, plane_id, new_data):
        self.plane_logic.update_plane(plane_id, new_data)

    def get_plane_statuses_at_time(self, input_time):
        return self.plane_logic.get_plane_statuses_at_time(input_time)
    
    def get_upcoming_flights_for_plane(self, plane_id):
        return self.flight_logic.get_upcoming_flights_for_plane(plane_id)

    """Flight related methods"""
    
    def add_flight(self, flight_data):
        self.flight_logic.add_new_flight(flight_data)

    def get_all_flights(self):
        return self.flight_logic.get_all_flights()

    def get_flight_by_id(self, flight_id):
        return self.flight_logic.get_flight_by_id(flight_id)

    def update_flight(self, flight_id, new_data):
        self.flight_logic.update_flight(flight_id, new_data)
    
    def validate_flight_creation(self, *args, **kwargs):
        return self.flight_logic.validate_flight_creation(*args, **kwargs)    

    def get_flights_by_date_with_manning_info(self, date):
        flights = self.flight_logic.get_flights_by_date(date)
        return [(flight, self.flight_logic.is_flight_properly_manned(flight.id)) for flight in flights]

    def get_flights_by_week_with_manning_info(self, start_date):
        flights = self.flight_logic.get_flights_by_week(start_date)
        return [(flight, self.flight_logic.is_flight_properly_manned(flight.id)) for flight in flights]
    
    """Flight employee assignment related methods"""
    
    def get_undermanned_flights(self):
        return [flight for flight in self.get_all_flights() if not self.flight_logic.is_flight_properly_manned(flight.id)]

    def get_available_pilots_for_flight(self, flight_id):
        flight = self.get_flight_by_id(flight_id)
        if not flight:
            return []
        return self.employee_logic.get_available_pilots(flight)

    def add_pilot_to_flight(self, flight_id, pilot_id):
        return self.employee_logic.add_pilot_to_flight(flight_id, pilot_id)

    def get_available_stewards_for_flight(self, flight_id):
        flight = self.get_flight_by_id(flight_id)
        if not flight:
            return []
        return self.employee_logic.get_available_stewards(flight)

    def add_steward_to_flight(self, flight_id, steward_id):
        return self.employee_logic.add_steward_to_flight(flight_id, steward_id)
