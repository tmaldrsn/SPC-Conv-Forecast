import time
import datetime

times = {1: ['0100', '1200', '1300', '1630', '2000'],
         2: ['0600', '1730'],
         3: ['0730']}

def geturl(outlook):
    """
    Retrieves the URL for the most recent outlook based on input:
        1 ==> Day 1
        2 ==> Day 2
        3 ==> Day 3
        48 ==> Days 4-8
    """

    current_time = time.gmtime(time.time())
    year = current_time.tm_year
    month = current_time.tm_mon
    day = current_time.tm_mday
    hour = current_time.tm_hour
    minute = current_time.tm_min

    if outlook == 1:
        if hour == 0:
            day -= 1
            hour = str("2000")
        elif 1 <= hour < 6:
            hour = str("0100")
        elif 6 <= hour < 13:
            hour = str("1200")
        elif 13 <= hour or (hour < 16 and minute < 30):
            hour = str("1300")
        elif (minute > 30 and 16 <= hour) or hour < 20:
            hour = str("1630")
        elif 20 <= hour <= 23:
            hour = str("2000")

        if month < 10:
            month = "0"+str(month)
        if day < 10:
            day = "0"+str(day)

        urlstring = "https://www.spc.noaa.gov/products/outlook/archive/{1}/KWNSPTSDY{0}_{1}{2}{3}{4}.txt".format(outlook, year, month, day, hour)

    elif outlook == 2:
        if hour < 6:
            day -= 1
            hour = str("1730")
        elif 6 <= hour <= 18:
            hour = str("0600")
        elif 18 < hour:
            hour = str("1730")

        if month < 10:
            month = "0"+str(month)
        if day < 10:
            day = "0"+str(day)

        urlstring = "https://www.spc.noaa.gov/products/outlook/archive/{1}/KWNSPTSDY{0}_{1}{2}{3}{4}.txt".format(outlook, year, month, day, hour)

    elif outlook == 3:
        hour = str("0730")

        if month < 10:
            month = "0"+str(month)
        if day < 10:
            day = "0"+str(day)

        urlstring = "https://www.spc.noaa.gov/products/outlook/archive/{1}/KWNSPTSDY{0}_{1}{2}{3}{4}.txt".format(outlook, year, month, day, hour)

    elif outlook == 48:
        if hour < 5:
            day -= 1
        if month < 10:
            month = "0"+str(month)
        if day < 10:
            day = "0"+str(day)

        urlstring = "https://www.spc.noaa.gov/products/exper/day4-8/archive/{1}/KWNSPTSD{0}_{1}{2}{3}.txt".format(outlook, year, month, day)

    return outlook, urlstring


def lookup_url(date, outlook, outlook_time):
    """
    Retrieves archived URL based on datetime.date object as input.
    """
    year = date.year
    month = date.strftime('%m')
    day = date.strftime('%d')

    if outlook == 48:
        urlstring = "https://www.spc.noaa.gov/products/exper/day4-8/archive/{1}/KWNSPTSD{0}_{1}{2}{3}.txt".format(outlook, year, month, day)
    else:
        urlstring = "https://www.spc.noaa.gov/products/outlook/archive/{1}/KWNSPTSDY{0}_{1}{2}{3}{4}.txt".format(outlook, year, month, day, outlook_time)

    return urlstring
