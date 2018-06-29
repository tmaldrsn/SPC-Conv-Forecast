import os
import json
import urllib.request
import requests
import conversion
import geturl

print("PACKAGES IMPORTED")

url = geturl.geturl()

print("URL RETREIVED")

text = urllib.request.urlopen(url).read().decode('utf-8')
text_array = list(filter(lambda a: a != '', text.split('\n')))

torn = text_array.index('... TORNADO ...')
hail = text_array.index('... HAIL ...')
wind = text_array.index('... WIND ...')
cate = text_array.index('... CATEGORICAL ...')
end = text_array[cate:].index("&&")

coords = {    "tornado":        text_array[torn+1:hail-1],
            "hail":            text_array[hail+1:wind-1],
            "wind":            text_array[wind+1:cate-2],
            "categorical":    text_array[cate+1:cate+end]}

probs = {    "tornado":        ["0.02", "0.05", "0.10", "0.15", "0.30", "0.45", "0.60", "SIGN"],
             "hail":            ["0.05", "0.15", "0.30", "0.45", "0.60", "SIGN"],
             "wind":            ["0.05", "0.15", "0.30", "0.45", "0.60", "SIGN"],
             "categorical":     ["TSTM", "MRGL", "SLGT", "ENH ", "MOD ", "HIGH"]}


def get_coordinates(event, probability):
    un_coords = coords[event]
    d = []
    for string in un_coords:
        new_string = list(filter(lambda a: a != '', string.split(' ')))
        d.append(new_string)

    indices = []
    for _ in range(len(d)):
        if d[_][0] in probs[event]:
            indices.append(_)

    low = min(i for i in range(len(d)) if d[i][0] == probability)
    high = max(i for i in range(len(d)) if d[i][0] == probability)

    try:
        while str(d[high+1][0]) not in probs[event]:
            high += 1
    except:
        pass

    i = low
    j = -1

    out = []
    while i <= high:
        if d[i][0] == probability:
            if "99999999" in d[i]:
                pass
            j += 1
            out.append([])
            new_out = out[j]
            new_out += d[i][1:]
        else:
            new_out += d[i][:]
        i += 1


    out = [[conversion.convert(coord) for coord in coords] for coords in out]
    return out
