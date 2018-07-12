import bordercoords
import get_coords as new
import conversion
from shapely.geometry import LineString
import matplotlib.pyplot as plt

def event_coords(prob):
	try:
		categorical = new.get_coordinates(event='severe', probability=prob)
		return categorical
	except ValueError:
		return False

def main():
	severe_005 = event_coords('0.05')
	severe_015 = event_coords('0.15')
	severe_030 = event_coords('0.30')
	severe_045 = event_coords('0.45')
	severe_060 = event_coords('0.60')
	severe_SIG = event_coords('SIGN')

	list = [severe_005, severe_015, severe_030, severe_045, severe_060, severe_SIG]
	colors = ['brown', 'yellow', 'red', 'pink', 'purple', 'black']
	for prob, color in zip(list, colors):
		if prob:
			for shape in prob:
				line = LineString(shape)
				plt.plot(line.xy[1], line.xy[0], color=color)


bordercoords.main()
main()
plt.show()
