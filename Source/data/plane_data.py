import csv

from ../model/plane_model import Plane 

class Plane_data():
    def __init__(self, csv_doc, model) -> None:
        self.csv_doc = csv_doc
        self.model = model
        self.data = []
        self.planeConstructor()

    def planeConstructor(self):
        """Reads plane data from the CSV and stores it as Plane objects."""
        with open(self.csv_doc, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                plane = Plane(
                    row['planeId'],
                    row['airlineName'],
                    row['airplaneModel'],
                    int(row['maxCapacity'])
                )
                self.data.append(plane)

    def addPlaneData(self, planeId, airlineName, airplaneModel, maxCapacity):
        """Adds a new plane's data to the CSV."""
        new_plane = Plane(planeId, airlineName, airplaneModel, maxCapacity)
        self.data.append(new_plane)
        with open(self.csv_doc, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_plane.get_plane_id(), new_plane.get_airline_name(), new_plane.get_airplane_model(), new_plane.get_max_capacity()])

    def modifyPlaneData(self, planeId, new_airlineName):
        """Modifies data in the CSV for a specific plane."""
        modified = False
        for plane in self.data:
            if plane.get_plane_id() == planeId:
                plane.set_airline_name(new_airlineName)
                modified = True
        
        if modified:
            with open(self.csv_doc, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['planeId', 'airlineName', 'airplaneModel', 'maxCapacity'])
                for plane in self.data:
                    writer.writerow([plane.get_plane_id(), plane.get_airline_name(), plane.get_airplane_model(), plane.get_max_capacity()])


plane_data = Plane_data("../files/planes.csv")

