import pandas as pd


df =pd.read_csv(r"C:\Users\vinee\Desktop\Github\money_in_politics\final.csv", sep = ",")


df.loc[df['ideology'] == "Pvt citizens", 'ideology'] = "Pvt"
df.to_csv(r"C:\Users\vinee\Desktop\Github\money_in_politics\final.csv", sep = ",",index=False)
