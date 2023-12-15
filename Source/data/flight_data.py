# flight_data.py
import csv
from model.flight_model import Flight
from datetime import datetime, timedelta

import csv
from model.flight_model import Flight
from datetime import datetime, timedelta

class Flight_Data:
    def __init__(self):
        self.model = "files/flights.csv"
        self.fieldname = ["id", "initial_location", "arrival_location", "employees", "plane", "start_home", "start_foreign", "tickets_home", "tickets_foreign"]

    def flight_constructor(self):
        flight_list = []
        with open(self.model, newline='', encoding="utf-8") as file:
            dict_file = csv.DictReader(file)
            for row in dict_file:
                # Split the 'employees' field using colons
                employees = [emp_id.strip() for emp_id in row["employees"].split(':')] if row["employees"] else []

                flight_list.append(Flight(
                    row["id"],
                    row["initial_location"],
                    row["arrival_location"],
                    employees,  # List of employee IDs
                    row["plane"],
                    row["start_home"],
                    row["start_foreign"],
                    int(row["tickets_home"]),
                    int(row["tickets_foreign"])
                ))
        return flight_list

    def add_flight_data(self, flight):
        with open(self.model, 'a', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file, fieldnames=self.fieldname)
            if file.tell() == 0:
                dict_write.writeheader()
            dict_write.writerow({
                "id": flight.id,
                "initial_location": flight.initial_location,
                "arrival_location": flight.arrival_location,
                "employees": ':'.join(flight.employees) if flight.employees else "",  # Join with colon
                "plane": flight.plane,
                "start_home": flight.start_home,
                "start_foreign": flight.start_foreign,
                "tickets_home": str(flight.tickets_home),
                "tickets_foreign": str(flight.tickets_foreign)
            })

    def modify_flight_data(self, flight_list):
        with open(self.model, 'w', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file, fieldnames=self.fieldname)
            dict_write.writeheader()
            for flight in flight_list:
                dict_write.writerow({
                    "id": flight.id,
                    "initial_location": flight.initial_location,
                    "arrival_location": flight.arrival_location,
                    "employees": ':'.join(flight.employees) if flight.employees else "",  # Join with colon
                    "plane": flight.plane,
                    "start_home": flight.start_home,
                    "start_foreign": flight.start_foreign,
                    "tickets_home": str(flight.tickets_home),
                    "tickets_foreign": str(flight.tickets_foreign)
                        })

    def get_flight_by_id(self, id):
        all_flights = self.flight_constructor()
        for flight in all_flights:
            if flight.id == id:
                return flight
        return None  

    
    def get_flights_by_date(self, date):
        all_flights = self.flight_constructor()
        return [flight for flight in all_flights if flight.start_home.startswith(date)]

    def get_flights_by_week(self, start_date):
        all_flights = self.flight_constructor()
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = start + timedelta(days=7)
        return [flight for flight in all_flights if start <= datetime.strptime(flight.start_home.split()[0], "%Y-%m-%d") < end]
