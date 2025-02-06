import numpy as np
import pandas as pd

if __name__ == "__main__":
    df1 = pd.read_csv('./IRS_Migration_Matrix_1990.csv')
    df1 = df1[['Unnamed: 0']]
    df2 = pd.read_csv('./../origin/CountyName_MSAName.csv')
    df2 = df2[['msa',  'msaname']]
    df2 = df2.drop_duplicates()
    df = df1.merge(df2, how='left', left_on= 'Unnamed: 0', right_on='msa')
    df[['msa',  'msaname']]
    __import__('pdb').set_trace()

