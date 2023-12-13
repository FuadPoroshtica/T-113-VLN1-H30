#plane_logic.py


from datetime import datetime, timedelta


class Plane_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def add_new_plane(self, plane):
        self.data_wrapper.add_plane(plane)

    def get_all_planes(self):
        return self.data_wrapper.get_all_planes()

    def get_plane_by_id(self, plane_id):
        return self.data_wrapper.get_plane_by_id(plane_id)

    def update_plane(self, plane_id, new_data):
        plane = self.get_plane_by_id(plane_id)
        if plane:
            for key, value in new_data.items():
                if value is not None:
                    setattr(plane, key, value)
            self.data_wrapper.modify_plane(plane)
    
    def get_plane_statuses_at_time(self, input_time):
        all_flights = self.data_wrapper.flight_data.flight_constructor()
        all_planes = self.get_all_planes()
        all_locations = self.data_wrapper.location_data.location_constructor()
        plane_statuses = []

        for plane in all_planes:
            status = "Not in use"
            for flight in all_flights:
                if flight.plane == plane.id:
                    start_home_dt = datetime.strptime(flight.start_home, "%Y-%m-%d %H:%M")
                    start_foreign_dt = datetime.strptime(flight.start_foreign, "%Y-%m-%d %H:%M")

                    arrival_location = next((loc for loc in all_locations if loc.airport_code == flight.arrival_location), None)
                    flight_duration = timedelta(minutes=arrival_location.flight_duration if arrival_location else 0)
                    turnaround_time = timedelta(hours=1)  # Assuming 1 hour turnaround


                    return_home_dt = start_foreign_dt + flight_duration

                    if start_home_dt <= input_time < start_foreign_dt - turnaround_time:
                        status = f"FLYING TO {flight.arrival_location}"
                        break
                    elif start_foreign_dt - turnaround_time <= input_time < (start_foreign_dt):
                        status = f"In {flight.arrival_location} for turnaround"
                        break
                    elif (start_foreign_dt) <= input_time < return_home_dt:
                        status = f"FLYING BACK TO {flight.initial_location}"
                        break

            plane_statuses.append(f"{plane.id}, {status}")

        return plane_statuses