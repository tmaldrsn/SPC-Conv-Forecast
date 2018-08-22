import os
import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing
from shapely.geometry import LineString
import bordercoords
import get_coords as new


def in_or_out(polygon, coordinates):
    polygon = np.array(polygon, np.float)
    try:
        lats = polygon[:, 0]
        lons = polygon[:, 1]
    except IndexError:
        return

    # determine number of horizontal intersections for coordinates

    current_lat = coordinates[0]
    current_lon = coordinates[1]

    count = 0
    for i in range(len(lats)-1):
        if lons[i] < current_lon or lons[i+1] < current_lon:
            continue
        else:
            check = (lats[i] - current_lat)*(lats[i+1] - current_lat)
            if check < 0:
                count += 1

    if count % 2 == 0:
        return False
    else:
        return True
