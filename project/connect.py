import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine('mysql+mysqlconnector://user@elk-2:Tn10z@6815@elk-2.mysql.database.azure.com:3306/azuredb')
#chunks = pd.read_csv(r'C:\Users\vinee\Desktop\Github\elk\datasets\fifa19\data.csv',sep=',',header=0, chunksize=18206)
chunks = pd.read_csv(r'C:\Users\vinee\OneDrive\Desktop\large scale visual analytics\project\CampaignFin18\pac18.csv',sep=',')

print(type(chunks))
chunks.to_sql(name='pac18', if_exists='replace', con=engine, index = False)


print("Done")

"""
with engine.connect() as con:
    rs = con.execute('SELECT * FROM cand WHERE FEC_ID = " H6FL08221 "')

for row in rs:
    print(row)
"""
