import numpy as np
import pandas as pd
import networkx as nx
from scipy.io import savemat

if __name__ == "__main__":
    years = [2018, 2019, 2020, 2021]
    dfs = []
    all_words = []
    for year in years:
        for month in range(1, 13):
            print('%d - %d' %  (year, month))
            df = pd.read_csv('./csv/%d_%d.csv'% (year, month))
            dfs.append(df)
            all_words.extend(list(df['Source']))
            all_words.extend(list(df['Target']))
    all_words = list(set(all_words))
    all_words.sort()

    Y = np.zeros((len(all_words), len(all_words), len(dfs)))
    for i, df in enumerate(dfs):
        G = nx.Graph()
        G.add_nodes_from(all_words)
        edges = zip(list(df['Source']), list(df['Target']), list(df['weight']))
        G.add_weighted_edges_from(edges)
        A = nx.adjacency_matrix(G)
        Y[:, :, i] = A.todense()
    Data = {'Y':Y,  'names':all_words}
    with open('./mat/data.mat', 'wb') as var:
        savemat(var, mdict=Data)



