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

