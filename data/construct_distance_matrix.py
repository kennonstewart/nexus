import numpy as np
import pandas as pd
from tqdm import tqdm

areas = ['06']
areas_names = ['CA']

df = pd.read_csv('dis.csv', dtype= {'county1' : str, 'county2' : str})
df = df[['county1', 'county2', 'mi_to_county']]

mask_from = df.county1.map(lambda x: x[:2] in areas)
mask_to = df.county2.map(lambda x: x[:2] in areas)

df_ = pd.read_csv('./migration_v2/%s/IRS_Migration_Matrix_1990.csv' % areas_names[0])
list_counties = list(df_.columns[1:])
list_counties = [('00000' + item)[-5:] for item in list_counties]

A = np.zeros((len(list_counties), len(list_counties)))
for i in range(A.shape[0]):
    print(i)
    for j in tqdm(range(A.shape[1])):
        dis = df.loc[(df.county1==list_counties[i]) & (df.county2==list_counties[j]), 'mi_to_county']
        if len(dis) > 0:
            A[i, j] = dis.iloc[0]

