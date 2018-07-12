import bordercoords
import get_coords as new
import conversion
import matplotlib.pyplot as plt
from shapely.geometry import LineString

def event_coords(prob):
	try:
		torn = new.get_coordinates(event='tornado', probability=prob)
		return torn
	except ValueError:
		return False

def main():
	torn_002 = event_coords('0.02')
	torn_005 = event_coords('0.05')
	torn_010 = event_coords('0.10')
	torn_015 = event_coords('0.15')
	torn_030 = event_coords('0.30')
	torn_045 = event_coords('0.45')
	torn_060 = event_coords('0.60')
	torn_SIG = event_coords('SIGN')

	list = [torn_002, torn_005, torn_010, torn_015, torn_030, torn_045, torn_060, torn_SIG]
	colors = ['green', 'brown', 'yellow', 'red', 'pink', 'purple', 'blue', 'black']
	for prob, color in zip(list, colors):
		if prob:
			for shape in prob:
				line = LineString(shape)
				plt.plot(line.xy[1], line.xy[0], color=color)

main()
bordercoords.main()
plt.show()
