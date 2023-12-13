#plane_data.py
import csv
from model.plane_model import Plane

class Plane_Data():
    def __init__(self) -> None:
        self.model = "files/planes.csv"
        self.fieldname = [
            "id",
            "airline_name",
            "airplane_model",
            "max_capacity"]

    def plane_constructor(self):
        plane_list = []
        with open(self.model, newline='', encoding="utf-8") as file:
            dict_file = csv.DictReader(file)
            for row in dict_file:
                plane_list.append(Plane(
                    row["id"],
                    row["airline_name"],
                    row["airplane_model"],
                    row["max_capacity"]))
        return plane_list

    def add_plane_data(self, plane):
        with open(self.model, 'a', newline='', encoding="utf-8") as file: 
            dict_write = csv.DictWriter(file, fieldnames=self.fieldname)
            if file.tell() == 0:  
                dict_write.writeheader()
            dict_write.writerow({
                "id": plane.id,
                "airline_name": plane.airline_name,
                "airplane_model": plane.airplane_model,
                "max_capacity": plane.max_capacity
            })

    def get_plane_by_id(self, id):
        all_planes = self.plane_constructor()
        for plane in all_planes:
            if plane.id == id:
                return plane
    
    def modify_plane_data(self,plane_list):
        with open(self.model,'w', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file,fieldnames=self.fieldname)
            dict_write.writerow({self.fieldname[i]: self.fieldname[i] for i in range(len(self.fieldname))})
            for plane in plane_list:
                dict_write.writerow({
                    "id":plane.id,
                    "airline_name":plane.airline_name,
                    "airplane_model":plane.airplane_model,
                    "max_capacity":plane.max_capacity
                    })      