#location_data.py

import csv
from model.location_model import Location

class Location_Data():
    def __init__(self) -> None:
        self.model = "files/locations.csv"
        self.fieldname = [
            "id",
            "country",
            "airport_code",
            "flight_duration",
            "distance",
            "manager_name",
            "emergency_phone"]

    def location_constructor(self):
        location_list = []
        with open(self.model, newline='', encoding="utf-8") as file:
            dict_file = csv.DictReader(file)
            for row in dict_file:
                location_list.append(Location(
                    row["id"],
                    row["country"],
                    row["airport_code"],
                    row["flight_duration"],
                    row["distance"],
                    row["manager_name"],
                    row["emergency_phone"]))
        return location_list

    def add_location_data(self, location):
        with open(self.model, 'a', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file, fieldnames=self.fieldname)
            if file.tell() == 0:  
                dict_write.writeheader()
            dict_write.writerow({
            "id": location.id,
            "country": location.country,
            "airport_code": location.airport_code,
            "flight_duration": location.flight_duration,
            "distance": location.distance,
            "manager_name": location.manager_name,
            "emergency_phone": location.emergency_phone
        })        

    def get_location_by_id(self, id):
        all_locations = self.location_constructor()
        for location in all_locations:
            if location.id == id:
                return location
        return None  
    
    def modify_location_data(self,location_list):
        with open(self.model,'w', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file,fieldnames=self.fieldname)
            dict_write.writerow({self.fieldname[i]: self.fieldname[i] for i in range(len(self.fieldname))})
            for location in location_list:
                dict_write.writerow({
                    "id":location.id,
                    "country":location.country,
                    "airport_code":location.airport_code,
                    "flight_duration":location.flight_duration,
                    "distance":location.distance,
                    "manager_name":location.manager_name,
                    "emergency_phone":location.emergency_phone
                    })      