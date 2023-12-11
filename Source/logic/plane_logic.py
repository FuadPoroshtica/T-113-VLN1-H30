
class Plane_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper
        
    def addPlane(self, plane):
        self.plane_data.add_plane(plane)
        
    
    def getPlanes(self):
        return self.plane_data.plane_constructor()

    def doesPlaneExist(self, plane_id):
        return any(Plane.id == plane_id for Plane in self.getPlanes())
            
    def searchPlane(self, plane_type):
        return [Plane for Plane in self.getPlanes() if plane_type in Plane.plane_type]

    def planeSort(self):
        return sorted(self.getPlanes(), key=lambda Plane: Plane.plane_type)
