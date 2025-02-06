import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy.io import savemat

YEARS = range(1990, 2019) #2019)

dfs = []
for i in YEARS:
    df_ = pd.read_csv('./../IRS_Migration_Matrix_%d.csv' % i,
                      header=0,
                      dtype={'Unnamed: 0': str})
    df_.index = df_['Unnamed: 0']
    df_.rename(columns={'Unnamed: 0': 'fipscounty'}, inplace=True)
    dfs.append(df_)


meta_df = pd.read_csv('./../origin/CountyName_MSAName.csv',
                      dtype={'fipscounty': str, 'msa':str} )
meta_df = meta_df.drop_duplicates()
meta_df = meta_df.dropna(subset=['msa'])

meta_df = meta_df.loc[meta_df.loc[:, 'msa'].map(lambda x: len(x))>2, :]
meta_df = meta_df[['fipscounty', 'msa', 'msaname']]
msa2fips = {}
for name, gr in meta_df.groupby('msa'):
    tmp = list(set(gr['fipscounty'].to_list()))
    msa2fips[name] = []
    for df in dfs:
        for fips in tmp:
            if fips in df.index:
                msa2fips[name].append(fips)
for k, v in msa2fips.items():
    msa2fips[k] = list(set(v))

df_tmp = meta_df[['msa',  'msaname']]
df_tmp = df_tmp.drop_duplicates()
msa2name = {a:b for a, b in zip(list(df_tmp['msa']), list(df_tmp['msaname']))}

num_msa = len(msa2fips)
list_msa = list(msa2fips.keys())
name_msa = [msa2name[item] for item in list_msa]
Y = np.zeros((len(list_msa), len(list_msa), len(dfs)))
# for i, df in tqdm(enumerate(dfs)):
#     dff = pd.DataFrame(np.zeros((num_msa, num_msa)),
#                        columns=list_msa,
#                        index=list_msa)
#     for transmitter in tqdm(list_msa):
#         for receiver in list_msa:
#             t_indices = msa2fips[transmitter]
#             r_indices = msa2fips[receiver]
#
#             np_node = df.loc[t_indices, r_indices].to_numpy()
#             if transmitter == receiver:
#                 dff.loc[transmitter, receiver] = np.sum(np_node) - np.sum(np.diagonal(np_node))
#             else:
#                 dff.loc[transmitter, receiver] = np.sum(np_node)
#
#     Y[:, :, i] = dff.to_numpy()

with open('./data2__.mat',  'wb') as o_f:
    savemat(o_f, mdict={'Y':Y, 'name': name_msa, \
            'counties': [msa2fips[item] if len(msa2fips[item])>0 else [''] for item in list_msa ]})

# dff.to_csv('./msa/IRS_Migration_Matrix_%d.csv' % YEARS[i])



# num_msa = len(msa2fips)
# list_msa = list(msa2fips.keys())
# for i, df in tqdm(enumerate(dfs)):
#     if i < 23:
#         continue
#     dff = pd.DataFrame(np.zeros((num_msa, num_msa)),
#                        columns=list_msa,
#                        index=list_msa)
#     for transmitter in list_msa:
#         for receiver in list_msa:
#             t_indices = msa2fips[transmitter]
#             r_indices = msa2fips[receiver]
#
#             np_node = df.loc[df.index.intersection(t_indices),
#                              df.index.intersection(r_indices)].to_numpy()
#             if transmitter == receiver:
#                 dff.loc[transmitter, receiver] = np.sum(np_node) - np.sum(np.diagonal(np_node))
#             else:
#                 dff.loc[transmitter, receiver] = np.sum(np_node)
#     dff.to_csv('./msa/IRS_Migration_Matrix_%d.csv' % YEARS[i])
#
# df.loc[df.index.intersection(['01000']), df.index.intersection(['01000'])]
#
# df.index.intersection(['01000'])
#
