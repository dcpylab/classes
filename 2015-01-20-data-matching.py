#!/usr/bin/env python
#
# Simple example of matching a couple of data sets 
# to create another data set
#
import csv

def read_file(name):
	with open(name, 'r') as input_file:
		reader = csv.DictReader(input_file, delimiter='|')
		data = []
		for row in reader:
			data.append(row)

	return data

data_files = [
	'name-address.psv',
	'name-bank-email.psv'
]

data_sets = {}

for filename in data_files:
	contents = read_file(filename)
	data_sets[filename] = contents

joined_data = {}
for data_set_name in data_sets:
	data_set = data_sets[data_set_name]
	for row in data_set:
		key = row['name']
		key = key.strip()
		key = key.lower()
		if key not in joined_data:
			joined_data[key] = row
		else:
			data = joined_data[key]
			data.update(row)

for row in joined_data.values():
	row_data = row.values()
	print "\t".join(row_data)

print len(joined_data)




