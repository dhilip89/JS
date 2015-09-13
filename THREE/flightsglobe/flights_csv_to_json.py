import csv

data_dict = {}
with open('start_dest_points.csv', 'rU') as infile:
    csvreader = csv.reader(infile)
    csvreader.next() # skip header row
    for row in csvreader:
        #count = int(row[2])
        lat, lon = row[3], row[2]
        #data_dict[lat, lon] = count
        data_dict[lat,lon] = 0.3

data = []
max_count = float(max(data_dict.values()))
for lat_lon, count in data_dict.items():
    data += lat_lon[0], lat_lon[1], str(count/max_count)

with open('flight_data.json', 'w') as outfile:
    outfile.write('[["counts",[{}]]]'.format(",".join(data)))