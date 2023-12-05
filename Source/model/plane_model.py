class Plane:
    def __init__(self, plane_id, airline_name, airplane_model, max_capacity):
        self.set_plane_id(plane_id)
        self.set_airline_name(airline_name)
        self.set_airplane_model(airplane_model)
        self.set_max_capacity(max_capacity)

    # Getter methods
    def get_plane_id(self):
        return self.plane_id

    def get_airline_name(self):
        return self.airline_name

    def get_airplane_model(self):
        return self.airplane_model

    def get_max_capacity(self):
        return self.max_capacity

    # Setter methods with type checking
    def set_plane_id(self, plane_id):
        if not isinstance(plane_id, str):
            raise ValueError("planeId must be a string")
        self.plane_id = plane_id

    def set_airline_name(self, airline_name):
        if not isinstance(airline_name, str):
            raise ValueError("airlineName must be a string")
        self.airline_name = airline_name

    def set_airplane_model(self, airplane_model):
        if not isinstance(airplane_model, str):
            raise ValueError("airplaneModel must be a string")
        self.airplane_model = airplane_model

    def set_max_capacity(self, max_capacity):
        if not isinstance(max_capacity, int):
            raise ValueError("maxCapacity must be an integer")
        self.max_capacity = max_capacity
