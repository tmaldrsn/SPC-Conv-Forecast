# import internal modules
import bordercoords
import get_forecast_object
import format_coordinates
import conversion

# import third-party modules
from shapely.geometry import LineString
import matplotlib
#matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


c = {
    "tornado": ['green', 'brown', 'yellow', 'red', 'pink', 'purple', 'blue', 'black'],
    "wind": ['brown', 'yellow', 'red', 'pink', 'purple', 'black'],
    "hail": ['brown', 'yellow', 'red', 'pink', 'purple', 'black'],
    "severe": ['brown', 'yellow', 'red', 'pink', 'purple', 'black'],
    "categorical": ['lime', 'green', 'yellow', 'orange', 'red', 'purple']
}


def main(forecast_object, event):
    """
    Plots the given forecast event based on a forecast object.
    """
    list = forecast_object["probs"][event]
    day = forecast_object["day"]
    colors = c[event]
    custom_lines = [Line2D([0], [0], color=color, lw=2) for color in colors]
    for prob, color in zip(list, colors):
        try:
            coords = format_coordinates.main(forecast_object, event=event, probability=prob)
        except ValueError:
            continue

        if coords:
            for shape in coords:
                line = LineString(shape)
                plt.plot(line.xy[1], line.xy[0], color=color)

#    plt.title("Probabilities")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(custom_lines, list, loc=4)

    bordercoords.main()
    plt.show()
