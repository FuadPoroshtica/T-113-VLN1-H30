#location_logic.py
class Location_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def verify_allowed(self, location, reason):
        #id,country,airport_code,flight_duration,distance,manager_name,emergency_phone
        location.country=location.country.title()
        location.airport_code=location.airport_code.upper()
        location.manager_name=location.manager_name.title()
        errors = []
        if reason == "add":
            if len(location.id) != 2:
                errors.append("Location Id needs to be 2 in length example(04)")

            elif any(location.id == x.id for x in self.get_all_locations()):
                errors.append(f"Location ID is already in use by {self.get_location_by_id(location.id).country}")

            if len(location.airport_code) != 3:
                errors.append("location code needs to be 3 characters")

            if len(location.airport_code).isalpha():
                errors.append("location code must only contain characters")

        if len(location.manager_name) >35:
            errors.append("Managers name is too long please no more than 35 characters")

        elif len(location.manager_name) <5:
            errors.append("Manager name needs to be atleast 5 characters")
        
        temp_cell=location.cell_phone.split(" ")
        if len(temp_cell) == 2:
            if "+" in temp_cell[0][0]: #allows "+" in verification
                temp_cell[0].pop("+")
            if temp_cell[0].isnumeric() == False or temp_cell[1].isnumeric() == False:
                errors.append("Please don't enter invalid characters")
        else:
            errors.append("Please have a space between numbers example(354 2000212)")

        if len(errors) != 0:
            return errors
    def add_new_location(self, location):
        condition = self.verify_allowed(location,"add")
        if type(condition) == type([]):
            return condition
        else:
            self.data_wrapper.add_location(location)
            return "Succesfully added location"

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
        condition = self.verify_allowed(location,"modify")
        if type(condition) == type([]):
            return condition
        else:
            for key, value in new_data.items():
                if value is not None:
                    setattr(location, key, value)
            self.data_wrapper.modify_location(location)
            return "Succesfully added plane"

