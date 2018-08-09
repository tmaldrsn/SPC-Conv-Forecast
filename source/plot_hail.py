import bordercoords
import get_coords as new
import conversion
from shapely.geometry import LineString
#import matplotlib
#matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def main(day=1):
    """
    Plots the hail probabilities for the Day 1 outlook.
    """
    
    list = ['0.05', '0.15', '0.30', '0.45', '0.60', 'SIGN']
    colors = ['brown', 'yellow', 'red', 'pink', 'purple', 'black']
    custom_lines = [Line2D([0], [0], color=color, lw=2) for color in colors]
    for prob, color in zip(list, colors):
        try:
            hail = new.get_coordinates(day, event='hail', probability=prob)
        except ValueError:
            continue

        if hail:
            for shape in hail:
                line = LineString(shape)
                plt.plot(line.xy[1], line.xy[0], color=color)

    plt.title("Hail Probabilities")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(custom_lines, list, loc=4)

    bordercoords.main()
    plt.show()


if __name__=='__main__':
    bordercoords.main()
    main()
    plt.show()
