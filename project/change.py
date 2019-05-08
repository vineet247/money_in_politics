import pandas as pd


df = pd.DataFrame(pd.read_csv(r"C:\Users\vinee\Desktop\Github\money_in_politics\final.csv", sep = ";"))


df.loc[df['ideology'] == "A", 'column_to_update'] = "Agriculture"
