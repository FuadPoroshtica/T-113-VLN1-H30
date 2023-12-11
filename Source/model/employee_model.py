#employee_model.py

class Employee:
    def __init__(self,id,name,address,cell_phone,email,title,home_phone="None",current_trip="None",plane_licenses="None") -> None:
        self.id = str(id)
        self.name = str(name)
        self.address = str(address)
        self.cell_phone = str(cell_phone)
        self.email = str(email)
        self.title = str(title)
        self.home_phone = str(home_phone)
        self.current_trip = current_trip
        self.plane_licenses = plane_licenses