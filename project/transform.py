import pandas as pd

file = pd.read_csv("final", sep = ",")
df = file.groupby(['Cand_ID','ideology','Cand_name','party']).agg({'Amt':sum}).reset_index()
df = df.set_index(['Cand_ID','Cand_name', 'party', 'ideology']).unstack(['ideology'])
df = df.fillna('0.0')
df.to_csv('output_data.csv',sep = ';')
