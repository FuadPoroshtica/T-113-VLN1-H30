#turn over time 60 minutes
#location_logic.py
class Flight_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def add_new_flight(self, flight):
        self.data_wrapper.add_flight(flight)
    
    def get_all_flights(self):
        return self.data_wrapper.get_all_flight()

    def get_flight_by_id(self, flight_id):
        return self.data_wrapper.get_location_by_id(flight_id)

    def update_location(self, flight_id, new_data):
        flight = self.get_location_by_id(flight_id)
        if flight:
            for key, value in new_data.items():
                if value is not None:
                    setattr(flight, key, value)
            self.data_wrapper.modify_location(flight)
