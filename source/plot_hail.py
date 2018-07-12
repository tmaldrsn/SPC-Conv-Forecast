import bordercoords
import get_coords as new
import conversion
from shapely.geometry import LineString
import matplotlib.pyplot as plt

def event_coords(prob):
	try:
		hail = new.get_coordinates(event='hail', probability=prob)
		return hail
	except ValueError:
		return False

def main():
	hail_005 = event_coords('0.05')
	hail_015 = event_coords('0.15')
	hail_030 = event_coords('0.30')
	hail_045 = event_coords('0.45')
	hail_060 = event_coords('0.60')
	hail_SIG = event_coords('SIGN')

	list = [hail_005, hail_015, hail_030, hail_045, hail_060, hail_SIG]
	colors = ['brown', 'yellow', 'red', 'pink', 'purple', 'black']
	for prob, color in zip(list, colors):
		if prob:
			for shape in prob:
				line = LineString(shape)
				plt.plot(line.xy[1], line.xy[0], color=color)


bordercoords.main()
main()
plt.show()
