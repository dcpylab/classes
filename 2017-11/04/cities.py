# make sure we can use this in all versions of Python
import csv
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

csv_url = "https://s3.amazonaws.com/necaris-miscellaneous/cities2.csv"
result = urlopen(csv_url)
raw_contents = result.read()
contents = raw_contents.decode('utf8', errors='ignore')
data = csv.DictReader(contents.split('\n'))
data = list(data)
# '2016 rank', 'City', 'State[5]', '2016 estimate', '2010 Census', 
# 'Change', '2016 land area', '2016 population density', 'Location'

sum_ = 0
count_ = 0
for row in data:
    population_as_string = row['2016 estimate']
    population_as_int = int(population_as_string.replace(',', ''))
    sum_ += population_as_int
    count_ += 1
print('Mean population:', sum_ / count_) 
