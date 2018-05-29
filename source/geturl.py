import time

def geturl():

	current_time = time.gmtime(time.time())

	year = current_time.tm_year
	month = current_time.tm_mon
	day = current_time.tm_mday
	hour = current_time.tm_hour

	if hour == 0:
		day -= 1
		hour = str("2000")
	elif 1 <= hour < 6:
		hour = str("0100")
	elif 6 <= hour < 12:
		hour = str("0600")
	elif 12 <= hour < 13:
		hour = str("1200")
	elif 13 <= hour < 17:
		hour = str("1300")
	elif 17 <= hour < 20:
		hour = str("1630")
	elif 20 <= hour <= 23:
		hour = str("2000") 


	if month < 10:
		month = "0"+str(month)
	if day < 10:
		day = "0"+str(day)


	urlstring = "http://www.spc.noaa.gov/products/outlook/archive/{0}/KWNSPTSDY1_{0}{1}{2}{3}.txt".format(year, month, day, hour)
	
	return urlstring

