class Flight:
    def __init__(self,id,initial_location,arrival_location,employees,plane,start_home,start_foreign,tickets_home,tickets_foreign) -> None:
        self.id = id
        self.initial_location = initial_location
        self.arrival_location = arrival_location
        self.employees = employees
        self.plane = plane
        self.start_home = start_home
        self.start_foreign = start_foreign
        self.tickets_home = tickets_home
        self.tickets_foreign = tickets_foreign
