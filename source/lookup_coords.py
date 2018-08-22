import logging

format = '%(asctime)-15s %(filename)s %(funcName)s %(message)s'
logging.basicConfig(filename='errlog.log', level=logging.DEBUG, format=format)


times = {1: ['0100', '0600', '1200', '1300', '1630', '2000'],
         2: ['0600', '1730'],
         3: ['0730']}


def get_coords(outlook, year, month, day, time):
    """
    Retrieves archived forecasts based on input date.
    """
    year = str(year)

    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)

    if day < 10:
        day = "0" + str(day)
    else:
        day = str(day)

    try:
        time = times[outlook][time]
    except KeyError, IndexError:
        raise

    urlstring = "https://www.spc.noaa.gov/products/outlook/archive/{1}/KWNSPTSDY{0}_{1}{2}{3}{4}.txt".format(outlook, year, month, day, time)

    logging.info("URL for {0} outlook on {1}/{2}/{3} retrieved.".format(times[outlook][time], month, day, year))
    return urlstring


def main():
    import sys
    if len(sys.argv) == 6:
        outlook = int(sys.argv[1])
        year = int(sys.argv[2])
        month = int(sys.argv[3])
        day = int(sys.argv[4])
        time = int(sys.argv[5])
        try:
            print(get_coords(outlook, year, month, day, time))
        except ArgumentError:
            pass

if __name__=='__main__':
    main()
