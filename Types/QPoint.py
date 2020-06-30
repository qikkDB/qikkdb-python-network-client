import logging
from Types.Point_pb2 import Point

class QPoint:
    def __init__(self, longitude, latitude):
        self.point = Point()
        self.point.geoPoint.longitude = longitude
        self.point.geoPoint.latitude = latitude

    def CreateFromWkt(wkt):
        p = QPoint(0, 0)
        wkt = wkt.replace("POINT(", "").replace("POINT (", "").replace(")", "")
        points = wkt.split(" ")
        if len(points) != 2:
            logging.error(f"Well known text polygon is in wrong format - wrong number of coordinates. [{wkt}]")
        try:
            latitude = float(points[0])
            longitude = float(points[1])
            p.point = Point()
            p.point.geoPoint.longitude = longitude
            p.point.geoPoint.latitude = latitude
        except Exception as e:
            logging.error(f"Error parsing wkt string. [{e}]")
        return p

