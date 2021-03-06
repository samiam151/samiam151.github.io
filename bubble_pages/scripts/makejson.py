#!/usr/bin/env python
import csv
import json

schools = {}
elementary_schools = []
middle_schools = []
joined_schools = []
high_schools = []
other = []

csvfile = '../data/DCPS_Master_114_sankey.csv'
with open(csvfile, 'rU') as file:
   reader = csv.DictReader(file)
   for row in reader:
      if row['Level'] == 'ES':
         elementary_schools.append(row['School'])
      elif row['Level'] == 'MS':
         middle_schools.append(row['School'])
      elif row['Level'] == 'HS':
         high_schools.append(row['School'])
      elif row['Level'] == 'ES/MS':
         joined_schools.append(row['School'])
      else:
         other.append(row['School'])


schools = {
   'elementary': elementary_schools,
   'middle': middle_schools,
   'high': high_schools,
   'joined': joined_schools,
   'other': other
}

data = json.dumps(schools)
with open('schools.json', 'w') as jsonFile:
   jsonFile.write(data)
