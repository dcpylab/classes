#!/usr/bin/env python
import pandas

data_files = [
	'name-address.psv',
	'name-bank-email.psv'
]

data_sets = []

for filename in data_files:
	data = pandas.read_csv(filename, delimiter='|')
	data_sets.append(data)

joined = pandas.merge(left=data_sets[0], right=data_sets[1],
	on='name', how='outer')
print joined

