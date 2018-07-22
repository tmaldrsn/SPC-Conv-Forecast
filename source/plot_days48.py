import bordercoords
import get_coords as new
import conversion
from shapely.geometry import LineString
#import matplotlib
#matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def main(day=48):
    list = ['D4', 'D5', 'D6', 'D7', 'D8']
    colors = ['red', 'purple', 'green', 'blue', 'brown']
    custom_lines = [Line2D([0], [0], color=color, lw=2) for color in colors]
    for prob, color in zip(list, colors):
        try:
            severe = new.get_coordinates(day, event='severe', probability=prob)
        except ValueError:
            continue

        if severe:
            for shape in severe:
                line = LineString(shape)
                plt.plot(line.xy[1], line.xy[0], color=color)

    plt.title("Categorical Outlook: DAYS 4-8")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.legend(custom_lines, list, loc=4)

    bordercoords.main()
    plt.show()

if __name__=='__main__':
    bordercoords.main()
    main()
    plt.show()
