import os, sys
from bs4 import BeautifulSoup
from shapely.geometry.polygon import Polygon, LinearRing
from shapely.geometry import LineString
import matplotlib.pyplot as plt
import checkpolygon

import logging

format = '%(asctime)-15s %(filename)s %(funcName)s %(message)s'
logging.basicConfig(filename='errlog.log', level=logging.DEBUG, format=format)

def out_of_boundaries(lat, lon):
    """
    Determines whether or not a given (latitude, longitude) coordinate pair
    is within the contiguous 48 states for plotting purposes
    """
    east_boundary = float(lon) < -125
    west_boundary = float(lon) > 10
    south_boundary = float(lat) < 20
    return east_boundary or west_boundary or south_boundary


def main():
    try:
        kml_file = './source/data/gz_2010_us_outline_20m.kml'
    except FileNotFoundError:
        kml_file = './data/gz_2010gz_2010_us_outline_20m.kml'

    logging.info("US KML file loaded.")

    with open(kml_file, 'r') as f:
        s = BeautifulSoup(f, 'lxml')
        finalstring = s.find_all('coordinates')

    for string in finalstring:
        polygon = []
        for coord in string:
            coord = str(coord).split(" ")
            lat = coord[0].split(",")[1]
            lon = coord[0].split(",")[0]
            if out_of_boundaries(lat, lon):
                continue
            for trip in coord:
                lon, lat, _ = trip.split(",")
                coordinate = (float(lat), float(lon))
                polygon.append(coordinate)
        try:
            polygon = LineString(polygon)
            plt.plot(polygon.xy[1], polygon.xy[0], color='b')
        except AttributeError:
            pass

    logging.info("US shape plotted.")


if __name__=='__main__':
    main()
