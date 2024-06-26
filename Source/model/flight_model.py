# flight_model.py

class Flight:
    def __init__(self, id, initial_location, arrival_location, employees, plane, start_home, start_foreign, tickets_home, tickets_foreign):
        self.id = str(id)
        self.initial_location = str(initial_location)
        self.arrival_location = str(arrival_location)
        self.employees = employees
        self.plane = str(plane)
        self.start_home = start_home  # Date and time in format 'YYYY-MM-DD HH:MM'
        self.start_foreign = start_foreign
        self.tickets_home = int(tickets_home)
        self.tickets_foreign = int(tickets_foreign)
