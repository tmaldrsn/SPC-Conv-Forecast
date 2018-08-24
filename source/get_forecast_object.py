import os
import urllib.request
import conversion
import geturl
import numpy as np
import logging


format = '%(asctime)-15s %(filename)s %(funcName)s %(message)s'
logging.basicConfig(filename='errlog.log', level=logging.DEBUG, format=format)


def main(days=1, url=None):
    """
    Retrieves and formats data from the current SPC forecast online.
    Also able to get information from any archived forecast URL.
    """

    if url is None:
        logging.info("No URL provided, extracting most recent available forecast.")
        day = geturl.geturl(days)[0]
        url = geturl.geturl(days)[1]
    else:
        logging.info("URL provided, attempting to extract archived forecast.")
        day = days
        url = url

    text = urllib.request.urlopen(url).read().decode('utf-8')
    text_array = list(filter(lambda a: a != '', text.split('\n')))

    logging.info("Forecast successfully retrieved.")

    if day == 1:
        torn = text_array.index('... TORNADO ...')
        hail = text_array.index('... HAIL ...')
        wind = text_array.index('... WIND ...')
        cate = text_array.index('... CATEGORICAL ...')
        end = text_array[cate:].index("&&")

        coords = {"tornado":        text_array[torn+1:hail-1],
                  "hail":           text_array[hail+1:wind-1],
                  "wind":           text_array[wind+1:cate-2],
                  "categorical":    text_array[cate+1:cate+end]}

        probs = {"tornado":         ["0.02", "0.05", "0.10", "0.15", "0.30", "0.45", "0.60", "SIGN"],
                 "hail":            ["0.05", "0.15", "0.30", "0.45", "0.60", "SIGN"],
                 "wind":            ["0.05", "0.15", "0.30", "0.45", "0.60", "SIGN"],
                 "categorical":     ["TSTM", "MRGL", "SLGT", "ENH", "MDT", "HIGH"]}
        logging.info('Day 1 outlook coordinates stored.')

    elif day == 2 or day == 3:
        severe = text_array.index('... ANY SEVERE ...')
        cate = text_array.index('... CATEGORICAL ...')
        end = text_array[cate:].index("&&")

        coords = {"severe":        text_array[severe+1:cate-2],
                  "categorical":   text_array[cate+1:cate+end]}

        probs = {"severe":        ["0.05", "0.15", "0.30", "0.45", "0.60", "SIGN"],
                 "categorical":   ["TSTM", "MRGL", "SLGT", "ENH ", "MDT ", "HIGH"]}

        logging.info('Day {} outlook coordinates stored.'.format(day))

    elif day == 48:
        severe = text_array.index('... ANY SEVERE ...')
        end = text_array[severe:].index("&&")

        coords = {"severe": text_array[severe+1:severe+end]}
        probs = {"severe": ['D4', 'D5', 'D6', 'D7', 'D8']}

        logging.info('Days 4-8 outlook coordinates stored.')

    forecast_object =  {
        "day": days,
        "coords": coords,
        "probs": probs
    }
    logging.info("Forecast object created.")

    return forecast_object

if __name__=='__main__':
    main()
