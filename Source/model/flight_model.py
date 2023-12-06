class Flight:
    def __init__(
        self,
        flightId,
        departure,
        arrival,
        employee,
        plane,
        startHomedate,
        starttime,
        returndate,
        returntime,
        ticketSold,
    ) -> None:
        self.flight_id = flightId
        self.departure = departure
        self.arrival = arrival
        self.employee = employee
        self.plane = plane
        self.startHomedate = startHomedate
        self.starttime = starttime
        self.returndate = returndate
        self.returntime = returntime
        self.ticketSold = ticketSold
