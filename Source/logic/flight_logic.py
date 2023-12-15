# flight_logic.py

from datetime import datetime, timedelta
from model.flight_model import Flight
from logic.date_converter import date_to_code


class Flight_Logic:
    def __init__(self, data_wrapper, location_logic, employee_logic):
        self.data_wrapper = data_wrapper
        self.location_logic = location_logic 
        self.employee_logic = employee_logic
    
    def add_new_flight(self, flight_data):
        start_home_dt = datetime.strptime(flight_data['start_home'], "%Y-%m-%d %H:%M")

        # Retrieve flight duration from arrival location
        arrival_location = self.location_logic.get_location_by_airport_code(flight_data['arrival_location'])
        if arrival_location:
            flight_duration = arrival_location.flight_duration
        else:
            flight_duration = 0 

        # Calculate start_foreign
        start_foreign_dt = start_home_dt + timedelta(minutes=flight_duration + 60)  # Add 60 minutes buffer
        flight_data['start_foreign'] = start_foreign_dt.strftime("%Y-%m-%d %H:%M")

        flight = Flight(
            flight_data['id'],
            flight_data['initial_location'],
            flight_data['arrival_location'],
            flight_data['employees'],
            flight_data['plane'],
            flight_data['start_home'],
            flight_data['start_foreign'],
            flight_data['tickets_home'],
            flight_data['tickets_foreign']
        )
        self.data_wrapper.add_flight(flight)


    def get_all_flights(self):
        return self.data_wrapper.get_all_flights()

    def get_flight_by_id(self, flight_id):
        return self.data_wrapper.get_flight_by_id(flight_id)

    def update_flight(self, flight_id, new_data):
        flight = self.get_flight_by_id(flight_id)
        if flight:
            for key, value in new_data.items():
                if value is not None:
                    setattr(flight, key, value)
            self.data_wrapper.modify_flight(flight)
    
    def get_next_flight_number(self, airline_code, location_id, date):
        all_flights = self.data_wrapper.get_all_flights()
        highest_number = 0
        for flight in all_flights:
            if (flight.id.startswith(f"{airline_code}{location_id}") and
                    flight.start_home.startswith(date)):
                current_number = int(flight.id[-3:])
                highest_number = max(highest_number, current_number)

        return str(highest_number + 1).zfill(3)
    
    def get_upcoming_flights_for_plane(self, plane_id):
        all_flights = self.data_wrapper.get_all_flights()
        current_time = datetime.now()
        upcoming_flights = [flight for flight in all_flights if flight.plane == plane_id and datetime.strptime(flight.start_home, "%Y-%m-%d %H:%M") > current_time]
        return upcoming_flights
    
    def generate_flight_id(self, plane, arrival_airport_code, start_home):
        airline_code = plane.airline_name[:2].upper()

        arrival_location = self.location_logic.get_location_by_airport_code(arrival_airport_code)
        if arrival_location:
            location_id = str(arrival_location.id).zfill(2)
        else:
            location_id = "00"

        start_time = datetime.strptime(start_home, "%Y-%m-%d %H:%M").strftime("%H%M")
        start_date = datetime.strptime(start_home.split(" ")[0], "%Y-%m-%d")
        date_string = date_to_code(start_date).upper()

        last_digits = self.generate_lowest_available_number(airline_code, location_id, start_home)

        return f"{airline_code}{location_id}{start_time}{date_string}{last_digits}"


    def generate_lowest_available_number(self, airline_code, location_id, start_home):
        all_flights = self.data_wrapper.get_all_flights()
        date_filter = start_home.split(" ")[0]
        existing_numbers = [int(flight.id[-2:]) for flight in all_flights if flight.id.startswith(f"{airline_code}{location_id}") and flight.start_home.startswith(date_filter)]
        existing_numbers.sort()

        lowest_number = 1
        for number in existing_numbers:
            if number != lowest_number:
                break
            lowest_number += 1

        return str(lowest_number).zfill(2)
    
    def _common_flight_validation(self, plane_id, start_home, arrival_airport_code, tickets_home, tickets_foreign):
        # Check for plane existence
        plane = self.data_wrapper.plane_data.get_plane_by_id(plane_id)
        if not plane:
            return False, "Plane not found."

        # Validate airport code and calculate total flight duration
        arrival_location = self.location_logic.get_location_by_airport_code(arrival_airport_code)
        if not arrival_location:
            return False, "Arrival airport code not found."
        total_duration = (2 * arrival_location.flight_duration) + 60  # 1 hour turnaround

        # Convert start_home to datetime and check format
        try:
            start_datetime, end_datetime = self._get_flight_datetime_range(start_home, total_duration)
        except ValueError:
            return False, "Invalid date/time format."

        # Validate and convert ticket numbers
        try:
            tickets_home = int(tickets_home)
            tickets_foreign = int(tickets_foreign)
        except ValueError:
            return False, "Invalid ticket count."

        # Check ticket numbers against plane capacity
        if tickets_home > int(plane.max_capacity) or tickets_foreign > int(plane.max_capacity):
            return False, "Ticket count exceeds maximum capacity."

        # Validate plane availability
        if not self._is_plane_available(plane_id, start_datetime, end_datetime):
            return False, "Plane not available for the entire duration of the flight."

        return True, "Validation successful."


    def _get_flight_datetime_range(self, start_home, total_duration):
        try:
            start_datetime = datetime.strptime(start_home, "%Y-%m-%d %H:%M")
            end_datetime = start_datetime + timedelta(minutes=total_duration)
            return start_datetime, end_datetime
        except ValueError:
            raise ValueError("Invalid date/time format.")

    def _is_plane_available(self, plane_id, start_datetime, end_datetime, current_flight_id=None):
        all_flights = self.data_wrapper.flight_data.flight_constructor()
        for flight in all_flights:
            if flight.plane == plane_id and flight.id != current_flight_id:
                flight_start = datetime.strptime(flight.start_home, "%Y-%m-%d %H:%M")
                arrival_location = self.location_logic.get_location_by_airport_code(flight.arrival_location)
                if arrival_location:
                    flight_duration = arrival_location.flight_duration
                else:
                    flight_duration = 0
                total_duration = (2 * flight_duration) + 60
                flight_end = datetime.strptime(flight.start_foreign, "%Y-%m-%d %H:%M") + timedelta(minutes=total_duration)

                if (flight_start <= start_datetime < flight_end) or (flight_start < end_datetime <= flight_end):
                    return False
        return True
    
    def validate_flight_creation(self, *args, **kwargs):
        return self._common_flight_validation(*args, **kwargs)
    
    def is_flight_properly_manned(self, flight_id):
        flight = self.get_flight_by_id(flight_id)
        if flight:
            pilots = [emp for emp in flight.employees if self.employee_logic.is_employee_a_pilot(emp)]
            stewards = [emp for emp in flight.employees if not self.employee_logic.is_employee_a_pilot(emp)]
            return len(pilots) >= 2 and len(stewards) >= 1
        return False
    
    def get_flights_by_date(self, date):
        return self.data_wrapper.get_flights_by_date(date)
    
    def get_flights_by_week(self, start_date):
        return self.data_wrapper.get_flights_by_week(start_date)