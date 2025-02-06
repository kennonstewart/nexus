import pandas as pd
import numpy as np
from scipy.io import savemat

years = range(1990, 2015, 5)
df = pd.read_csv('./csv/population.csv')
df_dict = pd.read_csv('./csv/world_dictionary.csv')
df = df.merge(df_dict, left_on='Country code', right_on='Numeric code', how='left')
df = df[~df['Alpha-3 code'].isna()]
# df.index = df['Alpha-3 code']

columns = ['Alpha-3 code'] + [str(y) for y in years]
df = df[columns]
df.index = df['Alpha-3 code']
df = df.drop(columns=['Alpha-3 code'])
for col in columns[1:]:
    df[col] = df[col].map(lambda x: ''.join([c for c in x if c!=' '])).astype(int)*1000
codename_to_population = df.to_dict('index')

dfs = []
data = np.zeros((199, 199, len(years)))

for i, y in enumerate(years):
    df_ = pd.read_csv('./csv/world_migration_time_%d.csv' % y)
    df_ = df_[df_['Unnamed: 0'] != 'CHI']
    df_.index = df_['Unnamed: 0']
    list_countries = list(df_['Unnamed: 0'])
    df_ = df_.drop(columns=['CHI', 'Unnamed: 0'])
    for name in list_countries:
        df_[name] = df_[name]/codename_to_population[name][str(y)]
    data[:, :, i] = df_.values

assert data.shape[0] == len(list_countries)
with open('./mat/world_norm_population.mat', 'wb') as o_f:
    savemat(o_f, {'data': data, 'countries':  list_countries})

