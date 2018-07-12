import bordercoords
import get_coords as new
import conversion
from shapely.geometry import LineString
import matplotlib.pyplot as plt

def event_coords(prob):
	try:
		wind = new.get_coordinates(event='wind', probability=prob)
		return wind
	except ValueError:
		return False

def main():
	wind_005 = event_coords('0.05')
	wind_015 = event_coords('0.15')
	wind_030 = event_coords('0.30')
	wind_045 = event_coords('0.45')
	wind_060 = event_coords('0.60')
	wind_SIG = event_coords('SIGN')

	list = [wind_005, wind_015, wind_030, wind_045, wind_060, wind_SIG]
	colors = ['brown', 'yellow', 'red', 'pink', 'purple', 'black']
	for prob, color in zip(list, colors):
		if prob:
			for shape in prob:
				line = LineString(shape)
				plt.plot(line.xy[1], line.xy[0], color=color)


bordercoords.main()
main()
plt.show()
