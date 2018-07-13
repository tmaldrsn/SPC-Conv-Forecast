import bordercoords
import get_coords as new
import conversion
import matplotlib.pyplot as plt
from shapely.geometry import LineString
from matplotlib.lines import Line2D

def event_coords(prob):
	try:
		torn = new.get_coordinates(event='tornado', probability=prob)
		return torn
	except ValueError:
		return False

def main():
	list = ['0.02', '0.05', '0.10', '0.15', '0.30', '0.45', '0.60', 'SIGN']
	colors = ['green', 'brown', 'yellow', 'red', 'pink', 'purple', 'blue', 'black']
	custom_lines = [Line2D([0], [0], color=color, lw=2) for color in colors]
	for prob, color in zip(list, colors):
		if event_coords(prob):
			for shape in event_coords(prob):
				line = LineString(shape)
				plt.plot(line.xy[1], line.xy[0], color=color)
		plt.legend(custom_lines, list, loc=4)

main()
bordercoords.main()
plt.show()
