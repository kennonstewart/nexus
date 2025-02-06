import pandas as pd

df = pd.read_csv('dis.csv', dtype= {'county1' : str, 'county2' : str})
df[ ['county1', 'county2', 'mi_to_county']].to_csv('dis.csv', index=None)

