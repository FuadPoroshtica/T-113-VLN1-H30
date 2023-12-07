from data.location_data import location_data

class Location_logic:
    def __init__(self):
        self.location_data = location_data()

    def getLocations(self):
        return self.location_data.location_constructor()

    def doesLocationExist(self, location_id):
        return any(Location.id == location_id for Location in self.getLocations())

    def changeSpecificLocation(self, location_id, updated_info):
        for Location in self.getLocations():
            if Location.id == location_id:
                Location.location_type = updated_info.get('location_type', Location.location_type)
                Location.manager_name = updated_info.get('manager_name', Location.name)
                Location.emergency_phone = updated_info.get('emergency_phone', Location.address)
                break   

    def searchLocation(self, location_type):
        return [Location for Location in self.getLocations() if location_type in Location.location_type]

    def locationSort(self):
        return sorted(self.getLocations(), key=lambda Location: Location.location_type)
