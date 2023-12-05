import csv

class location_data():
    def __init__(self, csv_doc, model) -> None:
        self.location = csv_doc
        self.model = model
        self.data = []
        self.locationConstructor()

    def locationConstructor(self):
        with open(self.location, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['airplaneModel'] == self.model:
                    self.data.append(row)

    def addLocationData(self, locationCodeId, country, airPort, flightTime, distanceFromIceland, managerName, EmergencyPhone):
        with open(self.location, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([locationCodeId, country, airPort, flightTime, distanceFromIceland, managerName, EmergencyPhone])

    def modifyLocationData(self, locationCodeId, new_data):
        with open(self.location, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        
        with open(self.location, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(reader.fieldnames)
            for row in rows:
                if row['locationCodeId'] == locationCodeId:
                    row.update(new_data)
                writer.writerow(row.values())
