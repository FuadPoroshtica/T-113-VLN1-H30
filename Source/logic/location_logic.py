class Location_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def add_new_location(self,id,country,airport_code,flight_duration,distance,manager_name,emergency_phone):
        self.data_wrapper.add_employee(id,country,airport_code,flight_duration,distance,manager_name,emergency_phone)

    def update_location(self, id, new_data):
        self.data_wrapper.modify_employee(id, new_data)


    #    def getLocations(self):
    #        return self.location_data.location_constructor()
    #
    #    def doesLocationExist(self, location_id):
    #        return any(Location.id == location_id for Location in self.getLocations())
    #
    #    def changeSpecificLocation(self, location_id, updated_info):
    #        for Location in self.getLocations():
    #            if Location.id == location_id:
    #                Location.manager_name = updated_info.get('manager_name', Location.name)
    #                Location.emergency_phone = updated_info.get('emergency_phone', Location.address)
    #                break
    #            
    #    def searchLocation(self, location_type):
    #        return [Location for Location in self.getLocations() if location_type in Location.location_type]
    #
    #    def locationSort(self):
    #        return sorted(self.getLocations(), key=lambda Location: Location.location_type)
    #print("1. Create New Location")
    #print("2. Modify Location")
    # 3. list locations