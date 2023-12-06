import csv
from model.plane_model import Plane

class plane_data():
    def __init__(self) -> None:
        self.model = "files/planes.csv"
        self.fieldname = ["id","country","airport_code","flight_duration","distance","manager_name","emergency_phone"]

    def plane_constructor(self):
        plane_list = []
        with open(self.model, newline='', encoding="utf-8") as file:
            dict_file = csv.DictReader(file)
            for row in dict_file:
                location_list.append(Plane(row["id"],row["country"],row["airport_code"],row["flight_duration"],row["distance"],row["manager_name"],row["emergency_phone"]))
        return location_list

    def add_plane_data(self,plane):
        with open(self.model, 'a', newline='', encoding="utf-8") as file:
            dict_write=csv.DictWriter(file,fieldname=self.fieldname)
            dict_write.writerow({})

    def modify_location_data(self,location_list):
        with open(self.model,'w', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file,fieldnames=self.fieldname)
            dict_write.writerow({self.fieldname[i]: self.fieldname[i] for i in range(len(self.fieldname))})
            for location in location_list:
                dict_write.writerow({"id":location.id,"country":location.country,"airport_code":location.airport_code,"flight_duration":location.flight_duration,"distance":location.distance,"manager_name":location.manager_name,"emergency_phone":location.emergency_phone})        
