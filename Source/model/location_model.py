#location_model.pt

class Location:
    def __init__(self, id, country, airport_code, flight_duration, distance, manager_name, emergency_phone):
        self.id = str(id)
        self.country = str(country)
        self.airport_code = str(airport_code)
        self.flight_duration = int(flight_duration)
        self.distance = float(distance)
        self.manager_name = str(manager_name)
        self.emergency_phone = str(emergency_phone)