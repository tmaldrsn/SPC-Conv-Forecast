import os
import urllib.request
import conversion
import geturl
import numpy as np
import logging


format = '%(asctime)-15s %(filename)s %(funcName)s %(message)s'
logging.basicConfig(filename='errlog.log', level=logging.DEBUG, format=format)


def remove_cont(coords_list, substr='99999999'):
    """
    Removes '99999999' ==> 'continue' coordinates in the forecast shapes where
    the outlook shapes reach the border and continue elsewhere on the border.
    """
    new_list = []
    for coord in coords_list:
        index = 0
        length = len(substr)
        while str.find(coord, substr) != -1:
            index = str.find(coord, substr)
            new_list.append(coord[0:index])
            coord = 'TSTM   ' + coord[index+length:]
        new_list.append(coord[:-1])
    return new_list


def main(info, event, probability, url=None):
    """
    Formats coordinates in form of nested arrays.
    """

    days = info["day"]
    coords = info["coords"]
    probs = info["probs"]
    logging.info("Information from retrieval script unpacked.")

    un_coords = remove_cont(coords[event])
    logging.info("CONTINUE coordinates removed from forecast.")

    d = []
    for string in un_coords:
        new_string = list(filter(lambda a: a != '', string.split(' ')))
        d.append(new_string)

    indices = []
    for _ in range(len(d)):
        if len(d[_]) != 0 and d[_][0] in probs[event]:
            indices.append(_)
        else:
            continue

    low = min(i for i in range(len(d)) if len(d[i]) != 0 and d[i][0] == probability)
    high = max(i for i in range(len(d)) if len(d[i]) != 0 and d[i][0] == probability)

    try:
        while len(d[high+1]) != 0 and str(d[high+1][0]) not in probs[event]:
            high += 1
    except IndexError:
        pass

    i = low
    j = -1

    out = []
    while i <= high:
        if len(d[i]) != 0 and d[i][0] == probability:
            j += 1
            out.append([])
            new_out = out[j]
            new_out += d[i][1:]
        else:
            new_out += d[i][:]
        i += 1

    out = [[conversion.convert(coord) for coord in coords] for coords in out]
    return out
