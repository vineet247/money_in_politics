import pandas as pd
import numpy as np

dataset = pd.read_csv(r'clustered_party.csv')

df2 = pd.melt(dataset, id_vars=['Name', 'Party'], var_name="ideology",value_name="Amt")
df2 = df2.fillna('0')
df2.to_csv(r'project\new_clustered_3.csv')
print(df2)
