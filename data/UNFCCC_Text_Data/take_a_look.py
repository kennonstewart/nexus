import pandas as pd

for year in range(16, 26):
    print(year)
    df = pd.read_csv('original_data/COP%dDTM.csv' % year)
    print('Original shape: ', df.shape)
    df = df.fillna(0)
    __import__('pdb').set_trace()
    df.to_csv('./clean_data/COP%dDTM.csv' % year, index=False)

