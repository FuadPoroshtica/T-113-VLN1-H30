#location_logic.py
class Location_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def add_new_location(self, location):
        self.data_wrapper.add_location(location)

    def get_all_locations(self):
        return self.data_wrapper.get_all_locations()

    def get_location_by_id(self, location_id):
        return self.data_wrapper.get_location_by_id(location_id)
    
    def get_location_by_airport_code(self, airport_code):
        all_locations = self.data_wrapper.get_all_locations()
        for location in all_locations:
            if location.airport_code == airport_code:
                return location
        return None

    def update_location(self, location_id, new_data):
        location = self.get_location_by_id(location_id)
        if location:
            for key, value in new_data.items():
                if value is not None:
                    setattr(location, key, value)
            self.data_wrapper.modify_location(location)
