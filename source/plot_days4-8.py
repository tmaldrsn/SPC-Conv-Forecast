import bordercoords
import get_coords as new
import conversion
from shapely.geometry import LineString
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def event_coords(prob):
	try:
		severe = new.get_coordinates(event='severe', probability=prob)
		return severe
	except ValueError:
		return False

def main():
	list = ['D4', 'D5', 'D6', 'D7', 'D8']
	colors = ['red', 'purple', 'green', 'blue', 'brown']
	custom_lines = [Line2D([0], [0], color=color, lw=2) for color in colors]
	for prob, color in zip(list, colors):
		if event_coords(prob):
			for shape in event_coords(prob):
				line = LineString(shape)
				plt.plot(line.xy[1], line.xy[0], color=color)
		plt.legend(custom_lines, list, loc=4)

bordercoords.main()
main()
plt.show()
