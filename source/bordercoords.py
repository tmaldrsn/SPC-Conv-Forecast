import os
from bs4 import BeautifulSoup
from shapely.geometry.polygon import Polygon, LinearRing
from shapely.geometry import LineString
import matplotlib.pyplot as plt


def main():
    print(os.getcwd())
    kml_file = './source/data/gz_2010_us_outline_20m.kml'

    f = open(kml_file, 'r')
    s = BeautifulSoup(f, 'xml')
    finalstring = s.find_all('coordinates')

    polygons = []

    start = 0
    fin = len(finalstring)

    for string in finalstring[start:fin]:
        polygon = []
        for coord in string:
            coord = str(coord).split(" ")
            east_boundary = float(coord[0].split(",")[0]) < -125
            west_boundary = float(coord[0].split(",")[0]) > 10
            south_boundary = float(coord[0].split(",")[1]) < 20
            if east_boundary or west_boundary or south_boundary:
                continue
            for trip in coord:
                lon, lat, _ = trip.split(",")
                coordinate = (float(lat), float(lon))
                polygon.append(coordinate)
        try:
            polygons.append(LineString(polygon))
        except ValueError:
            pass

    for i in range(fin-start):
        try:
            plt.plot(polygons[i].xy[1], polygons[i].xy[0], color='b')
        except AttributeError:
            pass
