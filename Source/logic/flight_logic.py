# flight_logic.py

from datetime import datetime, timedelta
from model.flight_model import Flight

class Flight_Logic:
    def __init__(self, data_wrapper, location_logic):
        self.data_wrapper = data_wrapper
        self.location_logic = location_logic 
    
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
            flight_data['start_foreign'],  # Use the provided start_foreign
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