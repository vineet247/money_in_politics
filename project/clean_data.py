import pandas as pd
from tabulate import tabulate
from csv import reader
"""
chunks = pd.read_csv(r'CampaignFin18\cand.csv',sep=',', chunksize=18206)

print(tabulate(chunks, headers='keys', tablefmt='psql'))
"""
file = open('CampaignFin18\cmtes18.txt')
nfile = open('CampaignFin18\cmtes18_test.txt', 'w')
for line in file:
	temp = line.replace(',,', ',| |,')
	temp = temp.replace(',,', ',| |,')
	temp = temp.replace('|,|', '|')
	nfile.write(temp)

nfile.close()
file.close()

