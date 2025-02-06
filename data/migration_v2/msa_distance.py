from itertools import product

from scipy.io import savemat
import numpy as np
import pandas as pd
from tqdm import tqdm

def get_distance_between(msa1, msa2, distance_master, msa_dict):
    """TODO: Docstring for get_distance_between.
    :returns: TODO

    """
    list_counties1 = msa_dict[msa1]
    list_counties2 = msa_dict[msa2]
    if len(list_counties1) == 0 or len(list_counties2) == 0:
        # Since we dont know, let say the distance is from the earth of outer space
        return 1000000000
    pairs = product(list_counties1, list_counties2)
    return np.mean([distance_master[pair] for pair in pairs])


if __name__ == "__main__":
    print('building msa dict')
    YEARS = range(1990, 2019)
    dfs = []
    for i in YEARS:
        df_ = pd.read_csv('origin/IRS_Migration_Matrix_%d.csv' % i,
                          header=0,
                          dtype={'Unnamed: 0': str})
        df_.index = df_['Unnamed: 0']
        df_.rename(columns={'Unnamed: 0': 'fipscounty'}, inplace=True)
        dfs.append(df_)

    meta_df = pd.read_csv('origin/CountyName_MSAName.csv',
                          dtype={'fipscounty': str, 'msa':str} )
    meta_df = meta_df.drop_duplicates()
    meta_df = meta_df.dropna(subset=['msa'])
    meta_df.loc[:, 'msa'].map(lambda x: len(x))>2
    sum(meta_df.loc[:, 'msa'] == '0040')
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
    sum([len(v) for k, v in msa2fips.items()])
    len(msa2fips)

    print('building distance master')
    df_tmp = pd.read_csv('./msa/IRS_Migration_Matrix_1990.csv')
    list_msa_code = list(df_tmp.columns)[1:]
    df_tmp = pd.read_csv('./../dis.csv', dtype={'county1' :str, 'county2' : str})
    tmp = zip(df_tmp.iloc[:, 0], df_tmp.iloc[:, 1], df_tmp.iloc[:, 2])
    distance_master = {(a, b): c for a,b,c in tmp}

    print('Building distance Q')
    Q = np.zeros((len(list_msa_code), len(list_msa_code)))
    for i in range(len(list_msa_code)):
        for j in range(0, i):
            Q[i, j] = get_distance_between(list_msa_code[i], list_msa_code[j], distance_master, msa2fips)
        Q[i, i] = 0

    for j in range(len(list_msa_code)):
        for i in range(0, j):
            Q[i, j] = Q[j, i]

    filename = './msa/dis.mat'
    with open(filename,  'wb') as f:
        mdict = {'Q' : Q}
        savemat(f, mdict)
    print('save to %s' % filename)


