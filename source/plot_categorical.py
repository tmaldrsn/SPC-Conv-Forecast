import bordercoords
import get_coords as new
import conversion
from shapely.geometry import LineString
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def main(day=1):
    list = ['TSTM', 'MRGL', 'SLGT', 'ENH ', 'MOD ', 'HIGH']
    colors = ['lime', 'green', 'yellow', 'orange', 'red', 'purple']
    custom_lines = [Line2D([0], [0], color=color, lw=2) for color in colors]
    for prob, color in zip(list, colors):
        try:
            categorical = new.get_coordinates(day, event='categorical', probability=prob)
        except ValueError:
            continue

        if categorical:
            for shape in categorical:
                line = LineString(shape)
                plt.plot(line.xy[1], line.xy[0], color=color)

    plt.title("Categorical Outlook: DAY " + str(day))
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(custom_lines, list, loc=4)

    bordercoords.main()
    plt.show()

if __name__=='__main__':
    bordercoords.main()
    main()
    plt.show()
