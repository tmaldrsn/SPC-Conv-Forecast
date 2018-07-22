import numpy as np


def convert(coords):
    lat = coords[:4]
    lon = coords[4:]

    lat = lat[:2] + "." + lat[2:]

    if int(lon[0]) > 5:
        lon = "-" + lon[:2] + "." + lon[2:]
    else:
        lon = "-1" + lon[:2] + "." + lon[2:]

    return (float(lat), float(lon))
