import os
import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing
from shapely.geometry import LineString
import bordercoords
import get_forecast_object

def get_coarse_us_coords_list():
    return [
        (47.46, -67.41),  (47.45, -69.26),  (45.52, -71.45),  (45.46, -75.15),
        (43.78, -76.89),  (43.74, -79.81),  (43.07, -79.54),  (41.97, -82.53),
        (43.58, -81.47),  (45.83, -82.09),  (48.86, -88.24),  (48.46, -89.47),
        (48.98, -93.96),  (49.61, -94.30),  (49.38, -123.57), (48.51, -123.75),
        (48.81, -125.08), (46.38, -124.54), (39.97, -125.07), (34.01, -121.11),
        (32.17, -117.33), (31.95, -114.70), (30.82, -110.79), (31.01, -106.79),
        (28.38, -103.67), (29.30, -102.04), (25.64, -99.40),  (25.40, -96.94),
        (27.14, -96.94),  (28.45, -95.44),  (29.07, -92.72),  (28.53, -90.61),
        (28.53, -88.33),  (29.76, -88.77),  (28.92, -83.76),  (24.39, -82.36),
        (24.38, -80.82),  (26.03, -79.32),  (31.20, -80.78),  (35.24, -75.06),
        (36.95, -75.23),  (40.18, -73.39),  (41.04, -69.19),  (43.58, -69.70),
        (44.61, -66.57),  (45.77, -67.32),
    ]

def plot_coarse_us_coords_list():
    shape = LinearRing(get_coarse_us_coords_list())
    plt.plot(shape.xy[1], shape.xy[0])


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
