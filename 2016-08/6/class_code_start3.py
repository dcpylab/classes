"""
Open DC Data - looking at Arts and Culture Organization 501(c)3 in the city
http://opendata.dc.gov/datasets/6321de8c38394f269937bb897f9a9853_52

Python 3
"""

# Starter Code
import os
import urllib.request
import csv

url = 'http://opendata.dc.gov/datasets/6321de8c38394f269937bb897f9a9853_52.csv'

filename = 'arts-and-culture-organizations.csv'

if not os.path.isfile(filename):
    print('file not found')
    urllib.request.urlretrieve(url, filename)
    # use requests if you have pip on your machine
else:
    # print('already here: ', filename)
    pass

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = []
    for row in reader:
        data.append(row)

        # print(row[6])
        # print(len(row))
# sample_data = data[0:4]
#
# print(sample_data[1][3])
# print(sample_data[1][6])

# print(len(data))

################## Counting Wards in DC ###########

# create an empty list
# ward_one = []
# ward_two = []
# count_ward_one = 0
# for row in data:
#     # print(row)
#     # print(row[11])
#     ward_number = row[11]
#     # if the ward in a row is 1,
#     if ward_number == '1':
#         # then add it to ward_one list
#         ward_one.append(row)
#         count_ward_one += 1
#
#     elif ward_number == '2':
#         ward_two.append(row)
#     # else ----- do nothing
#     else:
#         pass
# len function to count the number of elmentes in ward_one

from collections import Counter

all_wards = []

for row in data[1:]:
    all_wards.append(row[11])


c = Counter(all_wards)
print(c)




# c = Counter

# print(len(ward_two))

# sequence = ['a', 'b', 'c', 1.4, ['I', '2'], 2, 3, 4, 5, 6, 7]
# list_in_sequence = sequence[4]
# print(list_in_sequence[0])
#
# word_sequence = "I hope that it doesn't rain today."
# print(word_sequence[0:10])

# print(word_sequence[6:])

#     #X,Y,OBJECTID,NAME,ADDRESS,UNIT_SUITE,ZIP_4,CONTACT,SEC_NAME,NAICS,CENSUS_TRACT,WARD
#     #['-77.071611510121', '38.9076842758583', '434', 'SHAKESPEARE ASSOCIATION OF AMERICA', '37TH ST NW AND O STREET NW', '', '20057-0001', '', '', '813920', '000201', '2']
#     # f = open(filename, 'r').read()
#     # f.close()
#     # print(open_file_object)
