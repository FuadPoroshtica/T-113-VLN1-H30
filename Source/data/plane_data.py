import csv

class Plane_data():
    def __init__(self, csv_doc, model) -> None:
        self.plane = csv_doc
        self.model = model
        self.data = []
        self.planeConstructor()

    def planeConstructor(self):
        with open(self.plane, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data.append(row)

    def addPlaneData(self, planeId, airlineName, airplaneModel, maxCapacity):
        with open(self.plane, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([planeId, airlineName, airplaneModel, maxCapacity])

    def modifyPlaneData(self, planeId, new_airlineName):
        with open(self.plane, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        
        with open(self.plane, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(reader.fieldnames)
            for row in rows:
                if row['planeId'] == planeId:
                    row['airlineName'] = new_airlineName
                writer.writerow(row.values())
