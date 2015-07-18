#!/usr/bin/env python
#-*-coding: utf-8-*-
#
# Script to read and analyze sample bank data file
#
from __future__ import print_function, unicode_literals
import csv

# Load the data into memory from the CSV file
with open("sample_bank_data.csv", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    data = []

    for line in reader:
        line["balance"] = float(line["balance"])
        data.append(line)

# Work with the `data` array in memory
total = 0
for row in data:
    total = total + row["balance"]
    # total += row["balance"] # is equal

# Calculate the total wealth for each city, and display it in
# descending order
cities = {}
for row in data:
    city = row["city"]
    balance = row["balance"]

    if city not in cities:
        cities[city] = 0

    cities[city] += balance

cities_wealth = cities.items()
cities_wealth = sorted(cities_wealth, key=lambda pair: pair[1], reverse=True)

for info in cities_wealth:
    print(info)
