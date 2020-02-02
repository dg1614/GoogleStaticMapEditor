"""
	Author: Daniel Greenblatt
	Date: 	01/02/20
	Description: 
		To convert JSON map code into usable version for QGIS
"""

# Libraries
import sys
import re

def main():
	filename = "JSON_mapstyle.txt" #sys.argv[1]
	readfile(filename)

def readfile(filename):
	letter_test = re.compile("[a-z]+")
	code_string = "apistyle="
	input = ""

	with open(filename, 'r') as JSON:
		for l in JSON:
			if not letter_test.search(l):
				continue

			l = re.sub("[:\",\[\]]+", "", l)

			if "stylers" in l.split() :
				continue
			elif l.split()[1] in feature_type.keys() :
				input = input + feature_type["featureType"] + feature_type[l.split()[1]] + "|"
			elif l.split()[1] in element_type.keys() :
				input = input + element_type["elementType"] + element_type[l.split()[1]] + "|"
			elif l.split()[0] in styler_type.keys() :
				input = input + styler_type[l.split()[0]] + l.split()[1] + ","

				code_string = code_string + input
				input = ""
			else :
				print(l)
				print('Short code NOT found, skipping \n')

			
	code_string = code_string[:-1]
	print(code_string + "\n")


# Dictionary for conversion
feature_type = 	{	
					"featureType": "s.t:",
					"all": "0",
					"administrative": "1",
					"administrative.country": "17",
					"administrative.land_parcel": "21",
					"administrative.locality": "19",
					"administrative.neighborhood": "20",
					"administrative.province": "18",
					"landscape": "5",
					"landscape.man_made": "81",
					"landscape.natural": "82",
					"poi": "2",
					"poi.attraction": "37",
					"poi.business": "33",
					"poi.government": "34",
					"poi.medical": "36",
					"poi.park": "40",
					"poi.place_of_worship": "38",
					"poi.school": "35",
					"poi.sports_complex": "39",
					"road": "3",
					"road.arterial": "50",
					"road.highway": "49",
					"road.local": "51",
					"transit": "4",
					"transit.line": "65",
					"transit.station": "66",
					"water": "6",
				}

element_type = 	{
					"elementType": "s.e:",
					"geometry": "g",
					"geometry.fill": "g.f",
					"geometry.stroke": "g.s",
					"labels": "l",
					"labels.icon": "l.i",
					"labels.text": "l.t",
					"labels.text.fill": "l.t.f",
					"labels.text.stroke": "l.t.s",
				}

styler_type = 	{
					"color": "p.c:",
					"gamma": "p.g:",
					"hue": "p.h:",
					"invert_lightness": "p.il:",
					"lightness": "p.l:",
					"saturation": "p.s:",
					"visibility": "p.v:",
					"weight": "p.w:",
				}


if __name__ == "__main__" :
	main()
