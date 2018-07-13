times = {	1: ['0100', '0600', '1200', '1300', '1630', '2000'],
			2: ['0600', '1730'],
			3: ['0730']}

def get_coords(outlook, year, month, day, time):
	year = str(year)

	if month < 10:
		month = "0" + str(month)
	else:
		month = str(month)

	if day < 10:
		day = "0" + str(day)
	else:
		day = str(day)

	time = times[outlook][time]

	urlstring = "https://www.spc.noaa.gov/products/outlook/archive/{1}/KWNSPTSDY{0}_{1}{2}{3}{4}.txt".format(outlook, year, month, day, time)

	return urlstring