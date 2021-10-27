import csv
import pandas as pd

dataset_1 = 'bright_stars.csv'
dataset_2 = 'unit_converted_stars.csv'

d1 = []
d2 = []

with open(dataset_1, 'r', encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        d1.append(i)
    
        
with open(dataset_2, 'r', encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        d2.append(i)
    
headers_1 = d1[0]
stars_data_1 = d1[1:]

headers_2 = d2[0]
stars_data_2 = d2[1:]

headers = headers_1 + headers_2
stars_data = []

for i in stars_data_1:
    stars_data.append(i)
    
for j in stars_data_2:
    stars_data.append(j)

with open("total_stars.csv", "w", encoding = 'utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)
    
df = pd.read_csv('total_stars.csv')
df.tail(8)