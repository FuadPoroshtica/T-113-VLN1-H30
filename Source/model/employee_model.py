class Employee:
    def __init__(self,id,name,address,cell_phone,email,title,home_phone="None",current_trip="None",plane_licenses="None") -> None:
        self.id = id
        self.name = name
        self.address = address
        self.cell_phone = cell_phone
        self.email = email
        self.title = title
        self.home_phone = home_phone
        self.current_trip = current_trip
        self.plane_licenses = plane_licenses