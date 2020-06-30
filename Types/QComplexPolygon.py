import logging
from Types.ComplexPolygon_pb2 import ComplexPolygon, GeoPoint, Polygon
import re

MAX_POLYGONS_NUMBER = 8
regex = "((-?[0-9]+(\\.[0-9]+)?) (-?[0-9]+(\\.[0-9]+)?)(, ?)?)+"

class QComplexPolygon:
    def __init__(self):
        self.complexPolygon = ComplexPolygon()
        pass

    def CreateFromWkt(wkt):
        p = QComplexPolygon()
        geoPolygons = []
        polygons = []

        wkt = wkt.replace(", ", ",")
        polygons = wkt.split("),(")
        polygons = [i for i in polygons if i]

        polygons[0] = polygons[0].replace("POLYGON((", "").replace("POLYGON ((", "") #remove prefix
        polygons[len(polygons) - 1] = polygons[len(polygons) - 1].replace("))", "") #remove suffix

        if len(polygons) > MAX_POLYGONS_NUMBER:
            logging.error(f"Well known text polygon is in wrong format - encountered more polygons than is max number of polygons in complex polygon. [" + wkt + "]")

        print(polygons[0])

        for polygon in polygons:
            if ")" in polygon or "(" in polygon:
                logging.error(f"Well known text polygon is in wrong format - wrong number of '(' or ')'.")
            if re.match(regex, polygon) == False:
                logging.error(f"Well known text polygon is in wrong format - there is a wrong " + "character that is not a number, comma nor space. [" + wkt + "]")

            point = []
            points = polygon.split(",")

            geoPoints = []
            for point in points:
                coordinates = point.split(" ")
                if len(coordinates) > 2:
                    logging.error(f"Well known text polygon is in wrong format - wrong number of coordinates, there is more of them per geo point. [" + wkt + "]")
                try:
                    geoPoint = GeoPoint()
                    geoPoint.latitude = float(coordinates[0])
                    geoPoint.longitude = float(coordinates[1])
                    geoPoints.append(geoPoint)
                except Exception as e:
                    logging.error(f"Well known text polygon is in wrong format - encountered problem with geo point coordinates. [{e}]")

            geoPolygon = Polygon()
            geoPolygon.geoPoints.extend(geoPoints)
            geoPolygons.append(geoPolygon)
        #try:
        #except Exception as e:
        #    logging.error(f"Error parsing wkt string. [{e}]")
        complexPolygon = ComplexPolygon()
        complexPolygon.polygons.extend(geoPolygons)
        p.complexPolygon = complexPolygon
        return p

#p = QComplexPoint.CreateFromWkt("POLYGON((15.107421874999982 35.29986070530398,34.70703124999998 35.29986070530398,34.70703124999998 19.705148088048347,15.107421874999982 19.705148088048347,15.107421874999982 35.29986070530398))")
