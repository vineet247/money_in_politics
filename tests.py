import pandas as pd
import numpy as np

dataset = pd.read_csv(r'project\clustered_row.csv')

df2 = pd.melt(dataset, id_vars=['Origin','Name'], var_name="ideology",value_name="Amt")
df2.to_csv(r'project\new_clustered.csv')
print(df2)
