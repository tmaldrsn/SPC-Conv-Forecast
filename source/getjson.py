import os
import json
import urllib.request
import conversion
import geturl

print("PACKAGES IMPORTED")

url = geturl.geturl()

text = urllib.request.urlopen(url).read().decode('utf-8')
text_array = list(filter(lambda a: a != '', text.split('\n')))

torn = text_array.index('... TORNADO ...')
hail = text_array.index('... HAIL ...')
wind = text_array.index('... WIND ...')
cate = text_array.index('... CATEGORICAL ...')
end = text_array[cate:].index("&&")

coords = {	"tornado":		text_array[torn+1:hail-1],
			"hail":			text_array[hail+1:wind-1],
			"wind":			text_array[wind+1:cate-2],
			"categorical":	text_array[cate+1:cate+end]}

probs = {	"tornado":		["0.02", "0.05", "0.10", "0.15", "0.30", "0.45", "0.60", "SIGN"],
		 	"hail":			["0.05", "0.15", "0.30", "0.45", "0.60", "SIGN"],
		 	"wind":			["0.05", "0.15", "0.30", "0.45", "0.60", "SIGN"],
		 	"categorical": 	["TSTM", "MRGL", "SLGT", "ENH ", "MOD ", "HIGH"]}

coord_dict = {}

for event, coord in coords.items():
	coord_dict[event] = {}

for event, probabilities in probs.items():
	for probability in probabilities:
		coord_dict[event][probability] = []

for event, coord in coords.items():
	for coordinate in coord:
		if coordinate[:4] == "    ":
			prob = coord[coord.index(coordinate)-1][:4]
			coordinate = prob + coordinate[4:]
		if coordinate[:4] in probs[event]:
			for term in coordinate[7:].split(' '):
				coord_dict[event][coordinate[:4]].append(conversion.convert(term))


file = json.dumps(coord_dict, indent=4)

print(file)

"""
os.chdir('./data/')

f = open(url[-27:-4] + ".json", 'w')
f.write(file)
print("Data file written")
	
os.chdir('..')
"""