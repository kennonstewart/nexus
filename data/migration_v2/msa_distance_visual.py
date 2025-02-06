import numpy as np
import pandas as pd
from scipy.io import loadmat
import matplotlib.pyplot as plt


if __name__ == "__main__":
    with open('./msa/dis.mat', 'rb') as f:
        mdict = loadmat(f)
    Q = mdict['Q']
    df = pd.read_csv('./origin/CountyName_MSAName.csv', dtype= {'msa': str})
    msa2name = zip(df['msa'], df['msaname'])
    msa2name = {a: str(b)[:20] for (a,b) in msa2name}

    df = pd.read_csv('./msa/IRS_Migration_Matrix_1991.csv')
    list_msa_code = list(df.columns)[1:]

    fig, ax = plt.subplots()
    plt.imshow(np.log(Q+0.1), cmap='hot', interpolation='nearest')
    ax.set_xticklabels([msa2name[item] for item in list_msa_code])
    ax.set_yticklabels([msa2name[item] for item in list_msa_code])
    plt.colorbar()
    plt.show()
    __import__('pdb').set_trace()


