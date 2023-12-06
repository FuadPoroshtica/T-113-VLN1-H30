from data.employee_data import Employee_Data
from data.flight_data import Flight_Data
from data.location_data import Location_Data
from data.plane_data import Plane_Data

class Data_Wrapper:
    def __init__(self):
        self.employee_data = Employee_Data()
        self.flight_data =Flight_Data()
        self.location_data = Location_Data()
        self.plane_data = Plane_Data()