import bordercoords
import get_coords as new
import conversion
import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use("TkAgg")
from shapely.geometry import LineString
from matplotlib.lines import Line2D


def main(day=1, url=None):
    list = ['0.02', '0.05', '0.10', '0.15', '0.30', '0.45', '0.60', 'SIGN']
    colors = ['green', 'brown', 'yellow', 'red', 'pink', 'purple', 'blue', 'black']
    custom_lines = [Line2D([0], [0], color=color, lw=2) for color in colors]
    for prob, color in zip(list, colors):
        try:
            torn = new.get_coordinates(day, url, event='tornado', probability=prob)
        except ValueError:
            continue

        if torn:
            for shape in torn:
                line = LineString(shape)
                plt.plot(line.xy[1], line.xy[0], color=color)

    plt.title("Tornado Probabilities")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(custom_lines, list, loc=4)

    bordercoords.main()
    plt.show()


if __name__=='__main__':
    import sys
    bordercoords.main()
    if len(sys.argv) == 2 and sys.argv[1] in [1, 2, 3, 48]:
        main(day)
    else:
        main()
    plt.show()
