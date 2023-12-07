import csv
from model.flight_model import Flight

class flight_data():
    def __init__(self) -> None:
        self.model = "files/flights.csv"
        self.fieldname = ["id","initial_location","arrival_location","employees","plane","start_home","start_foreign","tickets_home","tickets_foreign"]

    def flight_constructor(self):
        flight_list = []
        with open(self.model, newline='', encoding="utf-8") as file:
            dict_file = csv.DictReader(file)
            for row in dict_file:
                flight_list.append(Flight(row["id"],row["initial_location"],row["arrival_location"],row["employees"],row["plane"],row["start_home"],row["start_foreign"],row["tickets_home"],row["tickets_foreign"],))
        return flight_list

    def add_flight_data(self, flight):
        with open(self.model, 'a', newline='', encoding="utf-8") as file:
            dict_write=csv.DictWriter(file,fieldname=self.fieldname)
            dict_write.writerow({"id":flight.id,"initial_location":flight.initial_location,"arrival_location":flight.arrival_location,"employees":flight.employees,"plane":flight.plane,"start_home":flight.start_home,"start_foreign":flight.start_foreign,"tickets_home":flight.tickets_home,"tickets_foreign":flight.tickets_foreign})        

    def modify_flight_data(self, flight_list):
        with open(self.model,'w', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file,fieldnames=self.fieldname)
            dict_write.writerow({self.fieldname[i]: self.fieldname[i] for i in range(len(self.fieldname))})
            for flight in flight_list:
                dict_write.writerow({"id":flight.id,"initial_location":flight.initial_location,"arrival_location":flight.arrival_location,"employees":flight.employees,"plane":flight.plane,"start_home":flight.start_home,"start_foreign":flight.start_foreign,"tickets_home":flight.tickets_home,"tickets_foreign":flight.tickets_foreign})        

