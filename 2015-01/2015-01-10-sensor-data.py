#!/usr/bin/python
#
# Look at sensor data and pull out gyro information
#
import re
import json

def get_target_field(line):
	float_fields = [float(x) for x in fields]
	target_field = float_fields[3]
	return target_field
	
converters = {
	"float": float,
	"int": int
}

def parse_line(line, header_data):
	line = line.strip()
	fields = line.split(",")
	data = {}
	for value, metadata in zip(fields, header_data):
		datatype, name = metadata
		converter = converters[datatype]
		value = converter(value)
		data[name] = value

	return data


LOG_FILE = "2015-01-10-log.txt"
OUTPUT_FILE = "2015-01-10-log.json"

with open(LOG_FILE, 'r') as log_file:
	log_lines = log_file.readlines()

header_line = log_lines[0]
log_lines = log_lines[1:]

first_dbl_quote = header_line.index('"') + 1
last_dbl_quote = len(header_line) - 3
header_fields = header_line[first_dbl_quote:last_dbl_quote]

header_fields = header_fields.split(',')
header_data = []
for field in header_fields:
	header_info = re.match("%(.*?)\((.*?)\)", field)
	header_data.append(header_info.groups())

data_rows = [parse_line(line, header_data) for line in log_lines]
absolute_numbers = [row['CorrectedGyroX'] for row in data_rows]

print max(absolute_numbers)

with open(OUTPUT_FILE, "w") as out_file:
	data_json = json.dumps(data_rows)
	out_file.write(data_json)


