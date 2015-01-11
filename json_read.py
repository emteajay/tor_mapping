import json
import csv
import urllib
import os
###
"""create empty lists to store data"""
lat_long = []
ip_list = []
###
"""open text from tor.py"""
j_data = open('tor_relays.txt')
data = json.load(j_data)
###
"""extract ip address and type of node"""
for i in data['relays']:
	ip_list.append((i['ip'], "type: " + i['type']))
ip_list_to_use = ip_list[:20]
###
"""ping Hostip API"""
for i in ip_list_to_use:
	response = urllib.urlopen('http://api.hostip.info/get_html.php?ip='+str(i[0])+'&position=True').read()
	lat_long.append(response + i[1])

"""check string"""
def check_string(search_string):
	if search_string == -1:
		return None, 0

b = open("output.csv", "w")
filewrite = csv.writer(b)

"""find Country, City, Laitude, Longitude, IP, and exit node type"""
for i in lat_long:
	# finders
	find_country = i.find("Country:")
	find_city = i.find("City:")
	find_latitude = i.find("Latitude:")
	find_longitude = i.find("Longitude:")	
	find_ip = i.find("IP:")
	find_type = i.find("type:")

	check_string(find_country)
	output_country = i[find_country + len("Country: ") : find_city - 6]

	check_string(find_city)
	output_city = i[find_city + len("City: ") : find_latitude - 2]

	check_string(find_latitude)
	output_latitude = i[find_latitude + len("Latitude: ") : find_longitude - 1]

	check_string(find_longitude)
	output_longitude = i[find_longitude + len("Longitude: ") : find_ip - 1]

	check_string(find_ip)
	output_ip = i[find_ip + len("IP: ") : find_type - 1]

	check_string(find_type)
	find_type_start = find_type + len("type: ")
	if i.find("normal") == True:
		find_type_end = find_type_start + 12
	else:
		find_type_end = find_type_start + 10	
	output_type = i[find_type_start:find_type_end]
	
	filewrite.writerow([output_country, output_city, output_latitude, output_longitude, output_ip, output_type])	

