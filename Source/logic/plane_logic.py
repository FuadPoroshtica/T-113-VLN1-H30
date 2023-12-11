#plane_logic.py
class Plane_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper
        
    def add_new_plane(self, plane):
        self.data_wrapper.add_plane(plane)

    def get_all_planes(self):
        return self.data_wrapper.get_all_planes()

    def get_plane_by_id(self, plane_id):
        return self.data_wrapper.get_plane_by_id(plane_id)

    def update_plane_details(self, plane_id, new_details):
        plane = self.get_plane_by_id(plane_id)
        if plane:
            for key, value in new_details.items():
                if value is not None:
                    setattr(plane, key, value)
            self.data_wrapper.modify_plane(plane)
