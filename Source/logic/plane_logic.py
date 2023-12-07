from data.plane_data import plane_data

class Plane_logic:
    def __init__(self):
        self.plane_data = plane_data()
    
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
