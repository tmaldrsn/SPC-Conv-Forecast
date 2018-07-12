import bordercoords
import get_coords as new
import conversion
from shapely.geometry import LineString
import matplotlib.pyplot as plt

def event_coords(prob):
	try:
		categorical = new.get_coordinates(event='categorical', probability=prob)
		return categorical
	except ValueError:
		return False

def main():
	categorical_TSTM = event_coords('TSTM')
	categorical_MRGL = event_coords('MRGL')
	categorical_SLGT = event_coords('SLGT')
	categorical_ENH  = event_coords('ENH ')
	categorical_MOD  = event_coords('MOD ')
	categorical_HIGH = event_coords('HIGH')

	list = [categorical_TSTM, categorical_MRGL, categorical_SLGT, categorical_ENH, categorical_MOD, categorical_HIGH]
	colors = ['lime', 'green', 'yellow', 'orange', 'red', 'purple']
	for prob, color in zip(list, colors):
		if prob:
			for shape in prob:
				line = LineString(shape)
				plt.plot(line.xy[1], line.xy[0], color=color)


bordercoords.main()
main()
plt.show()
