# location_logic.py
from model.location_model import Location

class Location_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def add_new_location(self, id, country, airport_code, flight_duration, distance, manager_name, emergency_phone):
        new_location = Location(id, country, airport_code, flight_duration, distance, manager_name, emergency_phone)
        self.data_wrapper.add_location(new_location)

    def update_location(self, id, new_data):
        location = self.get_location_by_id(id)
        if location:
            for key, value in new_data.items():
                setattr(location, key, value)
            self.data_wrapper.update_location(location)

    def get_all_locations(self):
        return self.data_wrapper.get_all_locations()

    def get_location_by_id(self, location_id):
        return self.data_wrapper.get_location_by_id(location_id)

    def update_location_details(self, location_id, new_details):
        location = self.get_location_by_id(location_id)
        if location:
            for key, value in new_details.items():
                if value is not None:
                    setattr(location, key, value)
            self.data_wrapper.modify_location(location)