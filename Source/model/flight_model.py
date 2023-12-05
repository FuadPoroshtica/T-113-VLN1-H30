class Flight:
    def __init__(self, flightId, location, employee, plane, startDateHome, startDateReturn, ticketSold) -> None:
        self.flight_id = flightId
        self.location = location
        self.employee = employee
        self.plane = plane
        self.startDateHome = startDateHome
        self.startDateReturn = startDateReturn
        self.ticketSold = ticketSold
